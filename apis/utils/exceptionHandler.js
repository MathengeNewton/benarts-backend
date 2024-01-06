const Sentry = require('@sentry/node');
const pkg = require('../package.json');

// Fastify Sentry hook
Sentry.init({
    dsn: process.env.SENTRY_DNS,
    environment: process.env.NODE_ENV,
    release: `upfield@${pkg.version}`
})


function SentryErrorLogging(error){
    if (process.env.NODE_ENV !== 'development') {
        Sentry.captureException(error);
    }
}

function captureBreadCramps(){
    Sentry.captureBreadCramps({
        message:"Seeding process failed.",
        category:"Database Issue",
        data:{
            time: newDate().toLocaleString()
        }
    })
}

module.exports = { SentryErrorLogging, captureBreadCramps };