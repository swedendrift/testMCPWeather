#!/usr/bin/env python3
"""
Weather MCP Client for Amazon Q CLI
This script demonstrates how to use the weather MCP server with Amazon Q CLI.
"""

import argparse
import json
import subprocess
import sys

def run_q_command(prompt, server_name="my-weather-server"):
    """Run Amazon Q CLI command with the specified prompt and server."""
    cmd = ["q", "chat", "--mcp-servers", server_name, prompt]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running Amazon Q CLI: {e}", file=sys.stderr)
        print(f"Error output: {e.stderr}", file=sys.stderr)
        sys.exit(1)

def get_weather_forecast(latitude, longitude):
    """Get weather forecast for a specific location."""
    prompt = f"Get the weather forecast for coordinates {latitude}, {longitude}"
    return run_q_command(prompt)

def get_weather_alerts(state):
    """Get weather alerts for a specific US state."""
    prompt = f"What are the current weather alerts for {state}?"
    return run_q_command(prompt)

def main():
    parser = argparse.ArgumentParser(description="Weather MCP Client for Amazon Q CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Forecast command
    forecast_parser = subparsers.add_parser("forecast", help="Get weather forecast")
    forecast_parser.add_argument("latitude", type=float, help="Latitude")
    forecast_parser.add_argument("longitude", type=float, help="Longitude")
    
    # Alerts command
    alerts_parser = subparsers.add_parser("alerts", help="Get weather alerts")
    alerts_parser.add_argument("state", type=str, help="Two-letter US state code (e.g., CA, NY)")
    
    args = parser.parse_args()
    
    if args.command == "forecast":
        print(get_weather_forecast(args.latitude, args.longitude))
    elif args.command == "alerts":
        print(get_weather_alerts(args.state))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()