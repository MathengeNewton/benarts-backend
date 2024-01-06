const c2bValidationSchema =  {
    tags: ['c2b Mpesa Validation'],
    consumes: ['multipart/form-data'],
    summary: 'C2B Mpesa validation URL.',
    body:{
        type:'object',
        properties : {
            transactionId: {type: 'string'},
            transactionAmount:{type:"string"},                    
            phoneNumber:{type:"string"},                    
        }
    }
};

module.exports = { 
    c2bValidationSchema
};
