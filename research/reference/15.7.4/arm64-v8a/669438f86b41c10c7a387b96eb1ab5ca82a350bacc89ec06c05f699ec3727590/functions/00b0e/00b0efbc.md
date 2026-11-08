# 00b0efbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00b0efbc",
  "name": "_ZN11flatbuffers6Parser12RecurseErrorEv",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c49598281e4c0d1cd3bbcf09819215abab35f636d3bfa1472655dd450159b91",
  "source_text_sha256": "2c49598281e4c0d1cd3bbcf09819215abab35f636d3bfa1472655dd450159b91"
}
~~~

## 呼び出し元

- [00bdf7f0](../00bdf/00bdf7f0.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb130](../00bdb/00bdb130.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00bdc180](../00bdc/00bdc180.md)
- [00bdf1a0](../00bdf/00bdf1a0.md)
- [00bdf9d0](../00bdf/00bdf9d0.md)

## 関連文字列（未確認候補）

~~~text
" reached"
"error: "
"maximum parsing recursion of "
~~~

## 疑似コード / UTF-8 2169 bytes

~~~c

void _ZN11flatbuffers6Parser12RecurseErrorEv(undefined2 *param_1,undefined8 param_2)

{
  long lVar1;
  ulong *puVar2;
  byte local_a8 [16];
  void *local_98;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  ulong local_70;
  ulong uStack_68;
  void *local_60;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_
            (local_a8,0x40);
  puVar2 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
                              (local_a8,0,"maximum parsing recursion of ",0x1d);
  uStack_88 = puVar2[1];
  local_90 = *puVar2;
  local_80 = (void *)puVar2[2];
  *puVar2 = 0;
  puVar2[1] = 0;
  puVar2[2] = 0;
  puVar2 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (&local_90," reached",8);
  uStack_68 = puVar2[1];
  local_70 = *puVar2;
  local_60 = (void *)puVar2[2];
  *puVar2 = 0;
  puVar2[1] = 0;
  puVar2[2] = 0;
                    /* try { // try from 00b0f054 to 00c0f06b has its CatchHandler @ 00b0fc00 */
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_50,"error: ",&local_70);
  _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_2,local_50);
                    /* try { // try from 00b0f06c to 00c0f0df has its CatchHandler @ 00b0ee6c */
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  *param_1 = 1;
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
                    /* try { // try from 00b0f0e0 to 00c0f0eb has its CatchHandler @ 00b0fbf8 */
  }
  if ((local_a8[0] & 1) != 0) {
    _ZdlPv(local_98);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0f0ec to 00c0f1a7 has its CatchHandler @ 00b0ee6c */
  __stack_chk_fail();
}

~~~
