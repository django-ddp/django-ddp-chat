if (Meteor.isClient) {

//User= new Mongo.Collection('auth.user');

Room= new Mongo.Collection('chat.room');
//Participant= new Mongo.Collection('chat.participant');
//Message= new Mongo.Collection('chat.message');

  // counter starts at 0
  RoomSub = Meteor.subscribe('PublicRooms');
  Session.setDefault('counter', 0);

  Template.body.helpers({
    rooms: function() {
      return Room.find({});
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
