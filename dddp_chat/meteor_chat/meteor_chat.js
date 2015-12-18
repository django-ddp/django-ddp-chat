auth = {
	User: new Mongo.Collection('auth.user')
};

chat = {
	Room: new Mongo.Collection('chat.room'),
	Participant: new Mongo.Collection('chat.participant'),
	Message: new Mongo.Collection('chat.message')
};

if (Meteor.isClient) {
  // counter starts at 0
  Meteor.subscribe('RoomRelated', 'django-ddp');
  Session.setDefault('counter', 0);

  Template.hello.helpers({
    counter: function () {
      return Session.get('counter');
    },
    rooms: function() {
      return chat.Room.find().fetch();
    }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set('counter', Session.get('counter') + 1);
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
