Set-Location F:\____IL_AI\PCM_RAG\lightrag
$env:Path = "F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts;$env:Path"
$env:NO_PROXY='*'
$env:TIKTOKEN_CACHE_DIR='C:\Users\il720506\AppData\Local\Temp\data-gym-cache'
$env:PYTHONIOENCODING='utf-8'
$env:MINERU_DEVICE_MODE='cuda'
& F:\____IL_AI\RAG\lightrag\.venv-rag\Scripts\python.exe rag_ingest.py "F:\____IL_AI\PCM_RAG\FOUND\Advances_in_Nanotechnology_in_PCM_and_Their_Applications.pdf" "F:\____IL_AI\PCM_RAG\FOUND\2-D_Numerical_Analysis_Of_The_Photovoltaic-Phase_Change_Material_PV-PCM_Model_With_Flat_Fi.pdf" "F:\____IL_AI\PCM_RAG\FOUND\Biomass_Ash_and_Phase_Change_Material_PCM_for_Energy_Efficiency_of_Sustainable_CementLime_.pdf" *>> F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log
$ec = $LASTEXITCODE
"EXITCODE=$ec" | Add-Content F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log
if ($ec -eq 0) { Remove-Item F:\____IL_AI\PCM_RAG\lightrag\LOG\ingest_run.log -Force }
