#version 330 core

layout (location = 0) in vec3 position;  
layout (location = 1) in vec2 texCoord;

uniform mat4 projection;
uniform mat3 normalMatrix;
uniform vec3 translation;

out vec2 v_texCoord;

void main()
{
  gl_Position = projection * vec4(position + translation, 1.0);
  v_texCoord = texCoord;  
}