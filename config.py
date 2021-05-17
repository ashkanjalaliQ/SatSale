# Bitcoin node connection settings
# This should point to your bitcoin/lnd node,
# with the correct RPC port as set in your config.
# Connecting through local host as  i'm running SatSale on my node
host = "127.0.0.1"
rpcport = "28256"

# From ~/.bitcoin/bitcoin.conf
username = "bitcoinrpc"
password = "RPCPASSWORD"

# Wallet ("" if single-wallet node, OR wallet name/path as shown in `biitcoin-cli listwallets`)
wallet = ""

# File in which API key will be stored
api_key_path = "SatSale_API_key"

# SSH tunnel to node (raspberry pi!)
# Make sure this command works `ssh HOST@IP -q -N -L 28256:localhost:28256`
# This forwards the ports required to talk to the node via RPC (or gRPC in the case of lightning)
# Use host = "127.0.0.1" and you will be able to see your node on 28256
tunnel_host = None  # "HOST@IP"

# Check for payment every xx seconds
pollrate = 15

# Payment expires after xx seconds
payment_timeout = 60*60

# Required confirmations for a payment
required_confirmations = 2

# Global connection attempts
connection_attempts = 3

# Generic redirect url after payment
redirect = "https://github.com/nickfarrow/btcpyment"

# Payment method
pay_method = "bitcoind"
# Switch payment_method to lnd if you want to use lightning payments instead. And uncomment lnd_dir.
#pay_method = "lnd"
# lnd_dir is only needed if you want to copy macaroon and TLS cert locally
#lnd_dir = "~/.lnd/"
#lnd_rpcport = "10009"
#lnd_macaroon = "invoice.macaroon"
#lnd_cert = "tls.cert"

# DO NOT CHANGE THIS TO TRUE UNLESS YOU WANT ALL PAYMENTS TO AUTOMATICALLY
# BE CONSIDERED AS PAID.
free_mode = False
