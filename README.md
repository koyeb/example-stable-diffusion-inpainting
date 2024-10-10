<div align="center">
  <a href="https://koyeb.com">
    <img src="https://www.koyeb.com/static/images/icons/koyeb.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Koyeb Serverless Platform</h3>
  <p align="center">
    Deploy Stable Diffusion on Koyeb
    <br />
    <a href="https://koyeb.com">Learn more about Koyeb</a>
    ·
    <a href="https://koyeb.com/docs">Explore the documentation</a>
    ·
    <a href="https://koyeb.com/tutorials">Discover our tutorials</a>
  </p>
</div>

## About Koyeb and the Stable Diffusion example application

Koyeb is a developer-friendly serverless platform to deploy apps globally. No-ops, servers, or infrastructure management.

This repository is designed to show how to deploy Stable Diffusion to Koyeb. The `Dockerfile` allows for configuration through environment variables to make deployment and configuration more straightforward.

## Getting Started

Follow the steps below to deploy Stable Diffusion to your Koyeb account.

### Requirements

To use this repository, you need:

- A Koyeb account to build the `Dockerfile` and deploy it to the platform. If you don't already have an account, you can [sign-up for free](https://app.koyeb.com/auth/signup).
- Access to GPU Instances on Koyeb.

### Deploy using the Koyeb button

The fastest way to deploy Stable Diffusion is to click the **Deploy to Koyeb** button below.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=stable-diffusion&type=git&repository=koyeb%2Fexample-stable-diffusion-inpainting&branch=main&builder=dockerfile&instance_type=gpu-nvidia-rtx-4000-sff-ada&ports=8000%3Bhttp%3B%2F)

Clicking on this button brings you to the Koyeb App creation page with most of the settings pre-configured to launch this application.

Additionally, open the **Health checks** section and set the **Grace period** to 300 seconds to allow time for vLLM to fetch the model.

_To modify this application example, you will need to fork this repository. Checkout the [fork and deploy](#fork-and-deploy-to-koyeb) instructions._

### Fork and deploy to Koyeb

If you want to customize and enhance this application, you need to fork this repository.

If you used the **Deploy to Koyeb** button, you can simply link your service to your forked repository to be able to push changes. Alternatively, you can manually create the application as described below.

On the [Koyeb Control Panel](https://app.koyeb.com/), on the **Overview** tab, click the **Create Web Service** button to begin.

1. Select **GitHub** as the deployment method.
2. Choose the repository containing your application code.
3. In the **Instance** section, select the **GPU** category and choose **RTX-4000-SFF-ADA**.
4. In the **Health checks** section, set the **Grace period** to 300 seconds. This will provide time for Stable Diffusion to download the appropriate model from Hugging Face and initialize the server.
5. Click **Deploy**.

The repository will be pulled, built, and deployed on Koyeb. Once the deployment is complete, it will be accessible using the Koyeb subdomain for your service.

## Contributing

If you have any questions, ideas or suggestions regarding this application sample, feel free to open an [issue](//github.com/koyeb/example-stable-diffusion-inpainting/issues) or fork this repository and open a [pull request](//github.com/koyeb/example-stable-diffusion-inpainting/pulls).

## Contact

[Koyeb](https://www.koyeb.com) - [@gokoyeb](https://twitter.com/gokoyeb) - [Slack](http://slack.koyeb.com/)
