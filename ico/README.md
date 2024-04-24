1. install, create new workspace (eth) and run Ganache versáo 2.1.1 (https://github.com/trufflesuite/ganache-ui/releases/download/v2.1.1/Ganache-2.1.1-win-x64.appx)
2. configure contract
	1. access https://remix.ethereum.org/#appVersion=0.7.7&optimize=false&version=soljson-v0.4.11+commit.68ef5810.js&lang=en&runs=200&evmVersion=null&language=Solidity
	2. create the rostcoin_ico.sol file
	3. in compile option, copy as bytecode
3. unzip myetherwallet
	1. open index.html
	2. add custom network / node
		node name = rostcoin
		url and port = rpc ganache server
	3. deploy new contract with copied contract bytecode
		1. select private key and get from Ganache from first account
	4. interact with contract
		1. go to ganache transactions and copy the CREATED CONTRACT ADDRESS from the transaction
		2. copy ABI from Remix
		3. click in access to see the read/write operations from this contract
