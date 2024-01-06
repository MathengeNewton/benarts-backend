const { validationUrlSchema } = require('../schema/index');
const { SentryErrorLogging } = require('../../utils/exceptionHandler');
const { nodeMailer } = require('../../utils/nodeMailer');

class mpesaHandler {

    async validationHandler(req,res){
        try{
            const request_object = req.body;
            const schemaValidation = validationUrlSchema.validate(request_object);         
            if (!schemaValidation.error){   
                const isValidBusinessCode = request_object.BusinessShortCode === process.env.BusinessShortCode ? true : false;
                if(isValidBusinessCode){                       
                    await req.prisma.UserLogs.create({
                        data:request_object
                    });                        
                    res.send({    
                        ResultCode: "0",
                        ResultDesc: "Accepted",
                    });
                }else{
                    res.send({
                        ResultCode: "C2B00011",
                        ResultDesc: "Rejected"
                    });
                }
            }else{  
                res.send({
                        ResultCode: "C2B00011",
                        ResultDesc: "Rejected"
                    });
            }   
        }catch(e){
            SentryErrorLogging(e);
            res.send({
                ResultCode: "C2B00011",
                ResultDesc: "Rejected"
            });
        }
    }

}

module.exports = {
    mpesaHandler    
};