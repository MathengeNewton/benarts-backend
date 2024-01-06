const { SentryErrorLogging } = require('../utils/exceptionHandler');
const env = require('dotenv').config({path: __dirname + '/../.env' });
const { hashPassword } = require('../utils/hash');

async function main(fastify){
    try{
        const password = await hashPassword(env.parsed.ADMIN_PASSWORD);
        const create_admin_user= {
            data: {
                username: env.parsed.ADMIN_USER,
                email: env.parsed.ADMIN_EMAIL,
                password: password.hash,
            }
        }
        const check_if_step_exist = await fastify.prisma.AdminUserModel.findMany({
            where:{
                email: env.parsed.ADMIN_EMAIL,
            }
        })
        if(!check_if_step_exist.length){
            await fastify.prisma.AdminUserModel.create(create_admin_user);
            console.log(`----User Created. Application will now run----`);
        }
        console.log(`----Seeding process complete. Application will now run----`);
    }catch(error){
        SentryErrorLogging(error)
        console.log(`Error: ${error}`)
        await fastify.prisma.$disconnect()
        process.exit(1)
    }
}

module.exports = { main };