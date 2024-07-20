from fastapi import FastAPI, File, UploadFile, Form, Header, Request
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status
import os 


# from Modules.Parent_Module.parent_module import Parent_Func
from app.Modules.Parent_Module.parent_module import Parent_Func
from app.Modules.Parent_Module.parent_module import Save_img_file

#Fast API Object
app = FastAPI() 

#Set CORS Origins
# origins = ["*"]  
# origins = ["http://localhost:3000/","http://localhost:4000"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"], 
#     # allow_headers=["Content-Type", "Authorization","Access-Control-Allow-Origin", "Access-Control-Allow-Credentials","application/json"]
#     ) 

@app.post('/nutritional_data_extraction') 
async def makeup_transfer(input_image: UploadFile = File(...)):
    '''
    #Write API description here
    Example: This API is for XYZ
    '''
    try:
        
        base_flag, input_image_path = Save_img_file(input_image)

        if base_flag:

            final_json = Parent_Func(input_image_path)

            data = {"status":200,"extracted_data":final_json}
            
            json_compatible_item_data = jsonable_encoder(data)
            
            return JSONResponse(
                content=jsonable_encoder(json_compatible_item_data),
                status_code=status.HTTP_200_OK,
            )
        
        else:

            data = {"status":400,"extracted_data":{}}
            
            json_compatible_item_data = jsonable_encoder(data)
            
            return JSONResponse(
                content=jsonable_encoder(json_compatible_item_data),
                status_code=status.HTTP_400_BAD_REQUEST,
            )



    except Exception as e:

        print("THIS IS THE EXCEPTION IN MAIN API",e)

        dic = {"status": 400, "extracted_data": "Some issue occured"}
        
        json_compatible_item_data = jsonable_encoder(dic)
        
        return JSONResponse(
            content=jsonable_encoder(json_compatible_item_data),
            status_code=status.HTTP_400_BAD_REQUEST,
        )

