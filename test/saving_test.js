const assert = require('assert');
const MarioChar = require('../models/mariochar');

// describe('testing mocha',function(){
//     it('adds numbers that equal to 5',function(){
//         assert(2+3===5);
//     });
// });

describe('Saving records',function(done){
    it('Saves record to database',function(){
        var char = new MarioChar({
            name:'Mario',
        });
        char.save().then(function(){
            assert(char.isNew === false);
            done();
        })       
     });
})