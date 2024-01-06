
const fastifyPrismaClient = require("fastify-prisma-client");

const fastifysecuresession = require('@fastify/secure-session');

const fs = require('fs');

const path = require('path');

const version = process.env.VERSION || 1 ;

const allRoutes = require('../routes/allRoutes');

const allPlugins = async (fastify) =>{   

    await  fastify.register(fastifysecuresession,{
        key: fs.readFileSync(path.join(__dirname, '../secret-key'))
    });

    await fastify.register(require('@fastify/cors'),{
        origin:true
    });        

    await fastify.register(require('fastify-bcrypt'), {
        saltWorkFactor: 12
    });    

    await  fastify.register(require('@fastify/multipart'), {
        addToBody: true
    });
    
    await fastify.register(require('@fastify/swagger'),{
        exposeRoute: true,
        routePrefix:process.env.SWAGGER_URL,
        swagger:{
            info:{
                title:process.env.APP_TITLE,
                description: process.env.APP_DESCRIPTION,
                version: version
            }
        },
        host: `localhost:${process.env.PORT}`,
        schemes: ['http'],
        consumes: ['application/json','multipart/form-data'],
        produces: ['application/json'],
    });
    
    await fastify.register(allRoutes,{prefix : `/api/v${version}/`})
    
    await fastify.register(fastifyPrismaClient,{});  
    await fastify.after();
    await fastify.ready();

}

module.exports = { allPlugins };