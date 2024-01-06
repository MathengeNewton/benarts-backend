const joi  = require('./entry');

const validationUrlSchema = joi.object({
    TransactionType: joi.string().required(),
    TransID: joi.string().required(),
    TransTime:joi.string().required(),
    TransAmount:joi.string().required(),
    BusinessShortCode: joi.string().required(),
    BillRefNumber:joi.string().required(),
    InvoiceNumber:joi.string().required(),
    OrgAccountBalance:joi.string().required(),
    ThirdPartyTransID: joi.string().required(),
    MSISDN:joi.string().required(),
    FirstName:joi.string().required(),
    MiddleName:joi.string().required(),
    LastName:joi.string().required()
})




module.exports = {
    validationUrlSchema
}