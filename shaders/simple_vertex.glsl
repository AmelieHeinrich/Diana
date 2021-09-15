#version 330 core

layout(location = 0) in vec3 aPos;
layout(location = 1) in vec2 aTexCoords;
layout(location = 2) in vec3 aNormals;

out vec2 fTexCoords;
out vec3 fNormals;
out vec3 fWorldPos;

uniform mat4 view_matrix;
uniform mat4 projection_matrix;
uniform mat4 model_matrix;
uniform mat4 transform_matrix;

void main()
{
	fNormals = mat3(model_matrix) * aNormals;
    fWorldPos = vec3(model_matrix * vec4(aPos, 1.0));
    fTexCoords = aTexCoords;

    gl_Position = projection_matrix * view_matrix * model_matrix * transform_matrix * vec4(fWorldPos, 1.0);    
}