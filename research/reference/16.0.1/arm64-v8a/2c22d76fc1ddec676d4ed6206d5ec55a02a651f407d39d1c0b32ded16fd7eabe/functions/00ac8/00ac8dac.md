# 00ac8dac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ac8dac",
  "name": "FUN_00ac8dac",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0055647895b1b708672bdcfa4161ba42d4c01526a2faea2639dba9694dd0fdb9",
  "source_text_sha256": "0055647895b1b708672bdcfa4161ba42d4c01526a2faea2639dba9694dd0fdb9"
}
~~~

## 呼び出し元

- [00789c50](../00789/00789c50.md)
- [0082ac68](../0082a/0082ac68.md)
- [0082cd18](../0082c/0082cd18.md)
- [008c5da4](../008c5/008c5da4.md)
- [00a75dac](../00a75/00a75dac.md)
- [00ac08fc](../00ac0/00ac08fc.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 328 bytes

~~~c

bool FUN_00ac8dac(long param_1)

{
  int iVar1;
  int iVar2;
  
  if ((*(char *)(param_1 + 0x3c) != '\0') && (iVar1 = *(int *)(param_1 + 0x68), iVar1 != 0)) {
    iVar2 = 0;
    if (iVar1 != 0) {
      iVar2 = *(int *)(param_1 + 0x4c) / iVar1;
    }
    return *(int *)(param_1 + 0x4c) != iVar2 * iVar1;
  }
  return false;
}

~~~
