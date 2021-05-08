const API_KEY = "YCI14HF7H55AB8QVDJ7TQ93HJ8J4DRC2ZX";
const MY_ADDRESS = "0x4159fCaEfD2216A1b581587cA97dA9F53e8ba163";
const MOONPIRATE_CONTRACT = "0xf09b7b6ba6dab7cccc3ae477a174b164c39f4c66";
console.log(API_KEY);

const tokenInfo = `https://api.bscscan.com/api?module=token&action=tokeninfo&contractaddress=${MOONPIRATE_CONTRACT}&apikey=${API_KEY}`;

//const API_CALL = `https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress=${MOONPIRATE_CONTRACT}&apikey=${API_KEY}`;

//"https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0xf09b7b6ba6dab7cccc3ae477a174b164c39f4c66&address=0x4159fCaEfD2216A1b581587cA97dA9F53e8ba163&tag=latest&apikey=YCI14HF7H55AB8QVDJ7TQ93HJ8J4DRC2ZX"
console.log(tokenInfo);

// @ts-ignore
var api = require("bscscan-api").init(API_KEY);
var supply = api.token;
console.log(supply);
