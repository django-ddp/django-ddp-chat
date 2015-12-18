(function(){

/////////////////////////////////////////////////////////////////////////
//                                                                     //
// meteor_chat.js                                                      //
//                                                                     //
/////////////////////////////////////////////////////////////////////////
                                                                       //
if (Meteor.isClient) {                                                 // 1
                                                                       //
  //User= new Mongo.Collection('auth.user');                           //
                                                                       //
  Room = new Mongo.Collection('chat.room');                            // 5
  //Participant= new Mongo.Collection('chat.participant');             //
  //Message= new Mongo.Collection('chat.message');                     //
                                                                       //
  // counter starts at 0                                               //
  RoomSub = Meteor.subscribe('PublicRooms');                           // 10
  Session.setDefault('counter', 0);                                    // 11
                                                                       //
  Template.body.helpers({                                              // 13
    rooms: function () {                                               // 14
      return Room.find({});                                            // 15
    }                                                                  //
  });                                                                  //
}                                                                      //
                                                                       //
if (Meteor.isServer) {                                                 // 20
  Meteor.startup(function () {                                         // 21
    // code to run on server at startup                                //
  });                                                                  //
}                                                                      //
/////////////////////////////////////////////////////////////////////////

}).call(this);

//# sourceMappingURL=meteor_chat.js.map
