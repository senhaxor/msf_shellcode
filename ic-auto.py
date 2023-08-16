import subprocess

repo_links = [
    "https://github.com/bats3c/ADCSPwn",
    "https://github.com/GhostPack/Certify",
    "https://github.com/mdsecactivebreach/Farmer",
    "https://github.com/GhostPack/Rubeus",
    "https://github.com/GhostPack/SafetyKatz",
    "https://github.com/GhostPack/Seatbelt",
    "https://github.com/slyd0g/SharpClipboard",
    "https://github.com/mandiant/SharPersist",
    "https://github.com/anthemtotheego/SharpExec",
    "https://github.com/FSecureLABS/SharpGPOAbuse",
    "https://github.com/BloodHoundAD/SharpHound",
    "https://github.com/djhohnstein/SharpLogger",
    "https://github.com/0xthirteen/SharpMove",
    "https://github.com/0xthirteen/SharpRDP",
    "https://github.com/G0ldenGunSec/SharpSecDump",
    "https://github.com/GhostPack/SharpUp",
    "https://github.com/tevora-threat/SharpView",
    "https://github.com/GhostPack/SharpWMI",
    "https://github.com/xforcered/StandIn",
    "https://github.com/djhohnstein/WireTap"
]

for repo_link in repo_links:
    # Extract repository name from URL
    repo_name = repo_link.split("/")[-1]
    
    # Create a directory for the repository
    subprocess.run(["mkdir", repo_name], check=True)
    
    # Clone the repository into the directory
    subprocess.run(["git", "clone", repo_link, repo_name], check=True)

print("All repositories cloned successfully.")
