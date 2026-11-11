# 00ac8dfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ac8dfc",
  "name": "FUN_00ac8dfc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56791046ae044d613b5ffc4e9046c995fdc495a36cf26e120260b1157c747b21",
  "source_text_sha256": "56791046ae044d613b5ffc4e9046c995fdc495a36cf26e120260b1157c747b21"
}
~~~

## 呼び出し元

- [00693458](../00693/00693458.md)
- [00788cac](../00788/00788cac.md)
- [0082cd18](../0082c/0082cd18.md)
- [008c385c](../008c3/008c385c.md)
- [008c5208](../008c5/008c5208.md)
- [00a6fd88](../00a6f/00a6fd88.md)
- [00a72594](../00a72/00a72594.md)
- [00a73530](../00a73/00a73530.md)
- [00a7c224](../00a7c/00a7c224.md)
- [00a7e564](../00a7e/00a7e564.md)
- [00ac0454](../00ac0/00ac0454.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 236 bytes

~~~c

void FUN_00ac8dfc(long param_1,int param_2)

{
  int iVar1;
  
  *(int *)(param_1 + 0x60) = param_2;
  iVar1 = -(*(int *)(param_1 + 0x68) * param_2);
  *(int *)(param_1 + 0x4c) = iVar1;
  *(int *)(param_1 + 0x50) = iVar1;
  return;
}

~~~
