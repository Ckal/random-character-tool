import requests
from transformers import Tool


class RandomCharatorGeneratorTool(Tool):
    name = "random_character"
    description = "This tool generates a random character. Returns json."

    inputs = ["text"]  # Adding an empty list for inputs

    outputs = ["json"]


    def __init__(self, device=None, **hub_kwargs) -> None:
        #if not is_accelerate_available():
        #    raise ImportError("Accelerate should be installed in order to use tools.")

        super().__init__()

        self.device = device
        self.pipeline = None
        self.hub_kwargs = hub_kwargs

    def setup(self):
        #if self.device is None:
        #    self.device = get_default_device()

        #self.pipeline = DiffusionPipeline.from_pretrained(self.default_checkpoint)
        #self.pipeline.scheduler = DPMSolverMultistepScheduler.from_config(self.pipeline.scheduler.config)
        #self.pipeline.to(self.device)

        #if self.device.type == "cuda":
        #    self.pipeline.to(torch_dtype=torch.float16)

        self.is_initialized = True

    def __call__(self, input:str="", *args, **kwargs):
        if not self.is_initialized:
            self.setup()
        
        API_URL = "https://randomuser.me/api/"
        
        response = requests.get(API_URL)
        data = response.json()['results'][0]

        # Extract the relevant character information
        character = {
            "gender": data['gender'],
            "name": {
                "title": data['name']['title'],
                "first": data['name']['first'],
                "last": data['name']['last']
            },
            "location": {
                "street": {
                    "number": data['location']['street']['number'],
                    "name": data['location']['street']['name']
                },
                "city": data['location']['city'],
                "state": data['location']['state'],
                "country": data['location']['country'],
                "postcode": data['location']['postcode'],
                "coordinates": {
                    "latitude": data['location']['coordinates']['latitude'],
                    "longitude": data['location']['coordinates']['longitude']
                },
                "timezone": {
                    "offset": data['location']['timezone']['offset'],
                    "description": data['location']['timezone']['description']
                }
            },
            "email": data['email'],
            "login": {
                "uuid": data['login']['uuid'],
                "username": data['login']['username'],
                "password": data['login']['password'],
                "salt": data['login']['salt'],
                "md5": data['login']['md5'],
                "sha1": data['login']['sha1'],
                "sha256": data['login']['sha256']
            },
            "dob": {
                "date": data['dob']['date'],
                "age": data['dob']['age']
            },
            "registered": {
                "date": data['registered']['date'],
                "age": data['registered']['age']
            },
            "phone": data['phone'],
            "cell": data['cell'],
            "id": {
                "name": data['id']['name'],
                "value": data['id']['value']
            },
            "picture": {
                "large": data['picture']['large'],
                "medium": data['picture']['medium'],
                "thumbnail": data['picture']['thumbnail']
            },
            "nat": data['nat']
        }

        return {"character": character}
