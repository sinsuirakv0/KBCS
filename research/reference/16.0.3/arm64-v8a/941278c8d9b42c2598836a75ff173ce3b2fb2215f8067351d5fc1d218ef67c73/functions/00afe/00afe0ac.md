# 00afe0ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afe0ac",
  "name": "FUN_00afe0ac",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e429987eafec3a27ce5d4a22fdf7ec15b329350b5dbc68a5b6fdb8edc607a29",
  "source_text_sha256": "7e429987eafec3a27ce5d4a22fdf7ec15b329350b5dbc68a5b6fdb8edc607a29"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 1532 bytes

~~~c

void FUN_00afe0ac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  int iVar3;
  
                    /* try { // try from 00afe0bc to 00bfe113 has its CatchHandler @ 00afe0bc
                       catch() { ... } // from try @ 00afe0bc with catch @ 00afe0bc
                       catch() { ... } // from try @ 00afe11c with catch @ 00afe0bc
                       catch() { ... } // from try @ 00afe15c with catch @ 00afe0bc */
  lVar1 = FUN_008524fc();
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008524fc();
    iVar3 = *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c);
  }
  else {
    iVar3 = 0;
  }
  lVar1 = FUN_008524fc();
                    /* try { // try from 00afe114 to 00bfe11b has its CatchHandler @ 00afe15c */
                    /* try { // try from 00afe11c to 00bfe153 has its CatchHandler @ 00afe0bc */
  uVar2 = FUN_005e7810(lVar1 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar2 & 1) == 0) {
    lVar1 = FUN_008524fc();
    *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a4c) = iVar3 + param_3;
  }
                    /* try { // try from 00afe154 to 00bfe15b has its CatchHandler @ 00afe15c */
                    /* catch() { ... } // from try @ 00afe114 with catch @ 00afe15c
                       catch() { ... } // from try @ 00afe154 with catch @ 00afe15c
                       try { // try from 00afe15c to 00bfe183 has its CatchHandler @ 00afe0bc */
  return;
}

~~~
