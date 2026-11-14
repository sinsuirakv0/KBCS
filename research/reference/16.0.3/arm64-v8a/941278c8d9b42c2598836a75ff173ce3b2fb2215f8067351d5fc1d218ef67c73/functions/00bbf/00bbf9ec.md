# 00bbf9ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbf9ec",
  "name": "_ZNK8firebase9messaging8internal13MessageReader29ConsumeUnregistrationReceivedEPKN3com6google8firebase9messaging3cpp32SerializedUnregistrationReceivedE",
  "size": 96,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ef8c9db34ef1f130ea2f14af4b37c3a29c57dce6d434ecf6a843126bdeeb318",
  "source_text_sha256": "0ef8c9db34ef1f130ea2f14af4b37c3a29c57dce6d434ecf6a843126bdeeb318"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1192 bytes

~~~c

void _ZNK8firebase9messaging8internal13MessageReader29ConsumeUnregistrationReceivedEPKN3com6google8firebase9messaging3cpp32SerializedUnregistrationReceivedE
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
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x30);
    }
    else {
      uVar3 = (ulong)((ushort *)((long)param_2 - (long)*param_2))[2];
      lVar4 = 0;
      if (uVar3 != 0) {
        puVar1 = (uint *)((long)param_2 + uVar3);
        lVar4 = (long)puVar1 + (ulong)*puVar1;
      }
      UNRECOVERED_JUMPTABLE = *(code **)(param_1 + 0x30);
    }
    if (UNRECOVERED_JUMPTABLE != (code *)0x0) {
      puVar2 = &DAT_002a64e6;
      if (lVar4 != 0) {
        puVar2 = (undefined1 *)(lVar4 + 4);
      }
                    /* WARNING: Could not recover jumptable at 0x00bbfa38. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (*UNRECOVERED_JUMPTABLE)(puVar2,*(undefined8 *)(param_1 + 0x38));
      return;
    }
  }
  return;
}

~~~
