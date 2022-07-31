# cat_or_dog
#### 2019 Autumn / Datacenter Programming / Term Project
###### 

## Docker-compose.yml
#### docker-compose.yml파일을 다운받아서 다음 명령어를 실행시키면 실행가능하다. 
<pre><code>docker-compose up</code></pre>

## 1_web
#### 사용자로부터 이미지를 받아오는 서버. 
#### http://localhost:5001/upload 로 접근

## 2_tensor
#### 컨테이너 안에서 미리 구현한 모델을 통해 받아온 이미지가 고양이인지 강아지인지 예측하는 서버.
#### 예측값을 제시한 후 맞는지 아닌지 물어본다. 

## 3_end
#### 예측값이 맞다면 1, 예측값이 틀렸다면 0을 record.txt에 저장한다. (예측시도 1번에 1번씩 저장된다. )
#### 다시 1로 돌아갈 것인지 물어본다. yes를 클릭하면 다시 1로 간다. 

## 0_result
#### 실제 사용자가 사용한 예측이 얼마나 맞았는지를 보여주는 서버. 
#### http://localhost:9000/result 로 접근
#### 수정) dockerhub에 올라와있는 yyi06011/0_result을 실행시키면 0.xxx%라고 나오는데, 0.xxx에서 100을 곱해야 맞는 수치임. 
