using Microsoft.AspNetCore.Mvc;
using BigCat3997.DemoLibrary.Dotnet6;

namespace Bigcat3997.DemoApp.Dotnet6.Controllers;

[ApiController]
[Route("")]
public class AppController : ControllerBase
{

    private readonly ILogger<AppController> _logger;

    public AppController(ILogger<AppController> logger)
    {
        _logger = logger;
    }

    [HttpGet(Name = "GetVersion")]
    [Route("version")]
    public string GetVersion()
    {
        return LibraryUtil.showMessage("Hello world!");
    }
}
