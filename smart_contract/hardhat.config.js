require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.18",
  networks: {
    sepolia: {
      url: "https://eth-sepolia.g.alchemy.com/v2/j5TF5A9Ho_jrS5srZH6Vjuqp3pVNdxkK",
      accounts: [process.env.PRIVATE_KEY],
    },
  },
};
