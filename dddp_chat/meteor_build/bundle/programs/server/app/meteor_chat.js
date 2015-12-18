(function(){

/////////////////////////////////////////////////////////////////////////
//                                                                     //
// meteor_chat.js                                                      //
//                                                                     //
/////////////////////////////////////////////////////////////////////////
                                                                       //
auth = {                                                               // 1
  User: new Mongo.Collection('auth.user')                              // 2
};                                                                     //
                                                                       //
chat = {                                                               // 5
  Room: new Mongo.Collection('chat.room'),                             // 6
  Participant: new Mongo.Collection('chat.participant'),               // 7
  Message: new Mongo.Collection('chat.message')                        // 8
};                                                                     //
                                                                       //
if (Meteor.isClient) {                                                 // 11
  // counter starts at 0                                               //
  Meteor.subscribe('RoomRelated', 'django-ddp');                       // 13
  Session.setDefault('counter', 0);                                    // 14
                                                                       //
  Template.hello.helpers({                                             // 16
    counter: function () {                                             // 17
      return Session.get('counter');                                   // 18
    },                                                                 //
    rooms: function () {                                               // 20
      return chat.Room.find().fetch();                                 // 21
    }                                                                  //
  });                                                                  //
                                                                       //
  Template.hello.events({                                              // 25
    'click button': function () {                                      // 26
      // increment the counter when button is clicked                  //
      Session.set('counter', Session.get('counter') + 1);              // 28
    }                                                                  //
  });                                                                  //
}                                                                      //
                                                                       //
if (Meteor.isServer) {                                                 // 33
  Meteor.startup(function () {                                         // 34
    // code to run on server at startup                                //
  });                                                                  //
}                                                                      //
/////////////////////////////////////////////////////////////////////////

}).call(this);

//# sourceMappingURL=meteor_chat.js.map
