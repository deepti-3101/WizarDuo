// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Certificate {
    address public authority;
    mapping (string => bool) public certificateIssued;

    modifier onlyAuthority() {
        require(msg.sender == authority, "Only the authority can perform this action");
        _;
    }

    modifier onlyAuthorizedDomain() {
        require(
            msg.sender == tx.origin ||
            msg.sender == authority ||
            isDomainAuthorized(msg.sender),
            "Unauthorized access from domain"
        );
        _;
    }

    constructor() {
        authority = msg.sender;
    }

    function issueCertificate(string memory _certificateHash) public onlyAuthorizedDomain {
        require(!certificateIssued[_certificateHash], "Certificate already issued");
        certificateIssued[_certificateHash] = true;
    }

    function isCertificateIssued(string memory _certificateHash) public view returns (bool) {
        return certificateIssued[_certificateHash];
    }

    mapping (address => bool) private authorizedDomains;

    function authorizeDomain(address _domain) public onlyAuthority {
        authorizedDomains[_domain] = true;
    }

    function deauthorizeDomain(address _domain) public onlyAuthority {
        authorizedDomains[_domain] = false;
    }

    function isDomainAuthorized(address _domain) public view returns (bool) {
        return authorizedDomains[_domain];
    }
}
