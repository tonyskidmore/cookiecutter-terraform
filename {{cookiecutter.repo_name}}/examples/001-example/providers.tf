terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=3.1.0"
    }
  }
  required_version = ">= 1.0.0"
  # backend "azurerm" {}
}