const assert = require('assert');
const MarioChar = require('../models/mariochar');

describe('Finding records',function(done){
    var char;
    beforeEach(function(done){
    char = new MarioChar({
        name:'Mario',
    });
    char.save().then(function(){
        assert(char.isNew === false);
        done();
    });   
});
    it('Find one record from database',function(){
        MarioChar.findOne({name:'Mario'}).then(function(result){
            assert(result.name === 'Mario');
            done();
        });
    });

    it('Find one record by ID from database',function(){
        MarioChar.findOne({_id:char._id}).then(function(result){
            assert(result.id.toString() === char._id.toString());
            done();
        });
    });
});