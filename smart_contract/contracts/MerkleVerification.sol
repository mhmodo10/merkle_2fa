// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract MerkleRootValidation {
    // bytes32 public merkleRoot;

    // constructor(bytes32 _merkleRoot) {
    //     merkleRoot = _merkleRoot;
    // }

    // function changeMerkleRoot(bytes32 _newMerkleRoot) public {
    //     merkleRoot = _newMerkleRoot;
    // }
    event VerificationResult(bool result,bytes32 message);

    function verify(bytes32 leaf, bytes32[] memory proof, bytes32 root) public {
        bool isValidProof = MerkleProof.verify(proof,root,leaf);
        // bytes32 computedHash = leaf;

        // for (uint256 i = 0; i < proof.length; i++) {
        //     bytes32 proofElement = proof[i];

        //     if (index % 2 == 0) {
        //         computedHash = sha256(abi.encodePacked(computedHash, proofElement));
        //     } else {
        //         computedHash = sha256(abi.encodePacked(proofElement, computedHash));
        //     }

        //     index = index / 2;
        // }
        bytes32 message = "";

        if(isValidProof){
            message = "Leaf is valid";
        } else {
            message = "Leaf is invalid";
        }
        emit VerificationResult(isValidProof,message);
    }
}
