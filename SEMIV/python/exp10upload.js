const AWS = require('aws-sdk');
const s3 = new AWS.S3();

exports.handler = async (event) => {
    const bucket = 'riyabucket';
    const dataToUpload = {
        PID: '2210488',
        DEPT: 'INFT',
        NAME: 'RIYA',
        FILE: 'ABC_111'
    };
    const fileName = 'ABC_111.json';
    const uploadByteStream = Buffer.from(JSON.stringify(dataToUpload), 'utf-8');

    const params = {
        Bucket: bucket,
        Key: fileName,
        Body: uploadByteStream
    };

    try {
        await s3.putObject(params).promise();
        console.log('Object has been uploaded');
    } catch (error) {
        console.error('Error uploading object:', error);
    }
};
