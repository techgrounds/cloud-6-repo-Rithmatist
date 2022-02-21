// This is sample Node.js code for AWS Lambda, to attach a secondary Elastic 
// Network Interface to an instance. To use this function, create an Auto Scaling
// lifecycle hook on instance creation notifying a SNS topic, and 
// subscribe the lambda function to the SNS topic.
// Sane values for Memory and Timeout are 128MB and 30s respectively.


var AWS = require('aws-sdk');
var ec2 = new AWS.EC2();
var as = new AWS.AutoScaling();

var async = require('async');

exports.handler = function (notification, context) {
  // Log the request
  console.log("INFO: request Recieved.\nDetails:\n", JSON.stringify(notification));
  var message = JSON.parse(notification.Records[0].Sns.Message);
  var metadata = JSON.parse(message.NotificationMetadata);
  console.log("DEBUG: SNS message contents. \nMessage:\n", message);
  console.log("DEBUG: Extracted Message Data\nData:\n", metadata);

  // Pull out metadata
  var instanceId = message.EC2InstanceId;
  var subnetId = metadata.SubnetId;
  var securityGroups = metadata.SecurityGroups;

  //define a closure for easy termination later on
  var terminate = function (success, err) {
    var lifecycleParams = {
      "AutoScalingGroupName" : message.AutoScalingGroupName,
      "LifecycleHookName" : message.LifecycleHookName,
      "LifecycleActionToken" : message.LifecycleActionToken,
      "LifecycleActionResult" : "ABANDON"
    };
    //log that we're terminating and why
    if(!success){
      console.log("ERROR: Lambda function reporting failure to AutoScaling with error:\n", err);
    }else{
      console.log("INFO: Lambda function reporting success to AutoScaling.");
      lifecycleParams.LifecycleActionResult = "CONTINUE";
    }
    //call autoscaling
    completeAsLifecycleAction (lifecycleParams, function lifecycleActionResponseHandler (err){
      if(err){
        context.fail();
      }else{
        //if we successfully notified AutoScaling of the instance status, tell lambda we succeeded
        //even if the operation on the instance failed
        context.succeed();
      }
    });
  }; 
    
  //Create the interface and wait for it to be ready
  createEni(subnetId, securityGroups, function CreateEniCallback(err, eniId){
    if(err){
      console.log("ERROR: Could not create ENI. Errors:\n", err);
      terminate(false,err);
    }
    //Wait for the ENI to be 'available'
    waitEniReady(eniId, function waitEniReadyCallback (err){
      if(err){
        console.log("ERROR: Failure waiting for ENI to be ready");
        terminate(false,err);
      }
      //attach it to the instance
      attachNetworkInterface(eniId, instanceId, function attachNetworkInterfaceCallback(err,data){
        if(err){
          console.log("ERROR: Could not attach ENI. Error Data:\n", err);
          terminate(false,err);
        }else{
          console.log("INFO: Successfully attached ENI");
          terminate(true, err);
        }
      });
    });
  });
};

function attachNetworkInterface (networkInterfaceId, instanceId, callback){
  //Attaches an ENI, passes the AttachmentId to callback.
  var nic_params = {
    'NetworkInterfaceId' : networkInterfaceId,
    'InstanceId' : instanceId,
    'DeviceIndex' : 1 // Should be safe to assume index 1 is available
  };
  ec2.attachNetworkInterface(nic_params, function evaluateEniAttachment(err,data) {
    if (err) {
      console.log("ERROR: ENI Attachment failed.\nDetails:\n", err);
      callback(err, null);
    } 
    console.log("INFO: ENI Attached.\nDetails:\n", data);
    callback(null, data.AttachmentId);
  });
}

function createEni(subnetId, securityGroups, callback){
  //Create a network interface, pass the Interface ID to callback 
  var eniCreationParams = {
    "SubnetId":subnetId,
    "Groups":securityGroups
  };
  console.log("DEBUG: CreateEni Params:\n",eniCreationParams);
  ec2.createNetworkInterface(eniCreationParams, function createEniCallback(err, data) {
    if (err) {
      console.log("ERROR: ENI creation failed.\nDetails:\n", err);
      return callback(err, null);
    } 
    console.log("INFO: ENI Created.\nData:\n", data);
    return callback(null, data.NetworkInterface.NetworkInterfaceId);
  });
}

function waitEniReady (eniId, waitEniReadyCallback){
  //terminate is the termination function if there's an issue.
  var getEniParams={
    "NetworkInterfaceIds":[
      eniId
    ]
  };
  console.log("INFO: Waiting on ENI to be ready:", eniId);
  var eniStatus = undefined;
  async.until(
    function isReady (err) { return eniStatus === "available"; },
    function getEniStatus(getEniStatusCallback){
      ec2.describeNetworkInterfaces(getEniParams,function handleGetEniResponse(err,data){
        eniStatus = data.NetworkInterfaces[0].Status;
        console.log("DEBUG: ENI status is:", eniStatus);
        getEniStatusCallback(err);
      });
    },
    function waitEniReadyCallbackClosure(err){
      if(err){
        console.log("ERROR: error waiting for ENI to be ready:\n",err);
      }
      waitEniReadyCallback(err);
    }
  );
}

function completeAsLifecycleAction(lifecycleParams, callback){
  //returns true on success or false on failure
  //notifies AutoScaling that it should either continue or abandon the instance
  as.completeLifecycleAction(lifecycleParams, function(err, data){
    if (err) {
      console.log("ERROR: AS lifecycle completion failed.\nDetails:\n", err);
      console.log("DEBUG: CompleteLifecycleAction\nParams:\n", lifecycleParams);
      callback(err);
    } else {
      console.log("INFO: CompleteLifecycleAction Successful.\nReported:\n", data);
      callback(null);
    }
  });
}