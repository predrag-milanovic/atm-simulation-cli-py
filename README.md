# ATM Simulation

A tiny command-line ATM simulator demonstrating basic Object-Oriented
Programming (OOP) concepts in Python. Users can check their balance,
deposit money, and withdraw funds through a simple interactive menu.

## Quick start

Requirements: Python 3.7+

Run the simulator:

```bash
python3 atm-simulation.py
```

## Interactive usage

When you run the program you will see a menu:

- `1` — Check Balance
- `2` — Deposit
- `3` — Withdraw
- `4` — Exit

Enter the number for the action you want and follow the prompts. Amounts
are accepted as numbers (decimals allowed) and the program validates
positive values and sufficient funds for withdrawals.

## Running automated (non-interactive) tests

There are no automated tests included in this minimal example. For a
production-ready project add a `tests/` directory and use `pytest` or
`unittest`.

## Optional Enhancements

• Implement a PIN system where users must enter their PIN before accessing the ATM functions.  
• Persist accounts between runs using a file or database so balances are retained across sessions.  
• Add support for multiple user accounts with authentication and per-account balances.  
• Track all transactions (deposits and withdrawals), generate receipts, and provide a viewable transaction history.  
• Provide a non-interactive CLI mode (flags/subcommands) for scripted or automated use.

## Contributing

Contributions are welcome. Fork the repository, make changes on a branch,
and open a pull request. Please include tests and keep changes focused.

All pull requests should be submitted to the `main` branch.

## License

See the [LICENSE](LICENSE) file for details.

