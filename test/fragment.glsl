#version 330 core

in vec2 v_texCoord;

uniform sampler2D texSampler;

layout (location = 0) out vec4 color;

void main()
{
  color = texture(texSampler, v_texCoord);
}