# 00bbe8fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bbe8fc",
  "name": "_ZNK8firebase9messaging8internal13MessageReader27ConsumeRegistrationReceivedEPKN3com6google8firebase9messaging3cpp30SerializedRegistrationReceivedE",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfb3b50a7acb9bebc29ad9ef1c0a9eadff231e56bf67a69ec6d823ba40eadb5f",
  "source_text_sha256": "bfb3b50a7acb9bebc29ad9ef1c0a9eadff231e56bf67a69ec6d823ba40eadb5f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1188 bytes

~~~c

void _ZNK8firebase9messaging8internal13MessageReader27ConsumeRegistrationReceivedEPKN3com6google8firebase9messaging3cpp30SerializedRegistrationReceivedE
               (long param_1,int *param_2)

{
  uint *puVar1;
  undefined1 *puVar2;
  code *UNRECOVERED_JUMPTABLE;
  ulong uVar3;
  long lVar4;
  
  if (param_2 != (int *)0x0) {
    if (*(ushort *)((long)param_2 - (long)*param_2) < 5) {
      lVar4 = 0;
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x20);
    }
    else {
      uVar3 = (ulong)((ushort *)((long)param_2 - (long)*param_2))[2];
      lVar4 = 0;
      if (uVar3 != 0) {
        puVar1 = (uint *)((long)param_2 + uVar3);
        lVar4 = (long)puVar1 + (ulong)*puVar1;
      }
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x20);
    }
    if (UNRECOVERED_JUMPTABLE != (code *)0x0) {
      puVar2 = &DAT_002a63ea;
      if (lVar4 != 0) {
        puVar2 = (undefined1 *)(lVar4 + 4);
      }
                    /* WARNING: Could not recover jumptable at 0x00bbe948. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (*UNRECOVERED_JUMPTABLE)(puVar2,*(undefined8 *)(param_1 + 0x28));
      return;
    }
  }
  return;
}

~~~
