const { mpesaHandler } = require("../../controllers/handler/mpesaHandler");
const  { 
    c2bValidationSchema,
} = require('../schema');

function authRoutes(fastify, options,done) {

    const userHandler = new UserHandler(fastify);   

    const c2bValidation = {
        schema:c2bValidationSchema,
        handler: userHandler.validationHandler
    };  

    fastify.post('/c2b-validation', c2bValidation);

    done();
    
}

module.exports =  authRoutes ;