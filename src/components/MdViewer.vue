<template>
  <div class="markdown-body">
    <Viewer :value="value" :plugins="plugins" />
  </div>
</template>

<script setup lang="ts">
import { Viewer } from "@bytemd/vue-next";
import gfm from "@bytemd/plugin-gfm";
import highlight from "@bytemd/plugin-highlight";
import "bytemd/dist/index.css";
import "highlight.js/styles/github.css";
import "github-markdown-css/github-markdown-light.css";

defineProps<{
  value: string;
}>();

const plugins = [gfm(), highlight()];
</script>
