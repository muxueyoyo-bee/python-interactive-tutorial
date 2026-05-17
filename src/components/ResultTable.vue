<template>
  <a-table
    v-if="columns.length > 0"
    :columns="columns"
    :data-source="dataSource"
    :pagination="{ hideOnSinglePage: true, pageSize: 20 }"
    size="small"
    bordered
  />
  <a-empty v-else description="无表格数据" />
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = defineProps<{
  data: Record<string, unknown>[];
}>();

const columns = computed(() => {
  if (props.data.length === 0) return [];
  return Object.keys(props.data[0]).map((key) => ({
    title: key,
    dataIndex: key,
    key,
    ellipsis: true,
  }));
});

const dataSource = computed(() =>
  props.data.map((row, i) => ({ ...row, _key: i }))
);
</script>
