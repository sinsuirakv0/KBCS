# 00bc8ffc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc8ffc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4413db116d566fa973c02549308ac3fe8dbe72bee6b8439c3030febb10fa69d",
  "source_text_sha256": "d4413db116d566fa973c02549308ac3fe8dbe72bee6b8439c3030febb10fa69d"
}
~~~

## 呼び出し元

- [00c5e760](../00c5e/00c5e760.md)

## 呼び出し先

- [00497da8](../00497/00497da8.md)
- [00bc90f0](../00bc9/00bc90f0.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c120](../00c5c/00c5c120.md)

## 関連文字列（未確認候補）

~~~text
"Remote Config: Failed to retrieve %s value from key %s"
"boolean"
~~~

## 疑似コード / UTF-8 952 bytes

~~~c

bool _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE
               (undefined8 *param_1,undefined8 param_2,long param_3)

{
  bool bVar1;
  char cVar2;
  char cVar3;
  long *plVar4;
  long lVar5;
  
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  lVar5 = FUN_00bc90f0(plVar4,param_1[0x33],param_2,param_3);
  bVar1 = false;
  if (lVar5 != 0) {
    cVar2 = FUN_00497da8(plVar4,lVar5,DAT_01127610);
    cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
    bVar1 = cVar3 == '\0';
    if (!bVar1) {
      (**(code **)(*plVar4 + 0x80))(plVar4);
      (**(code **)(*plVar4 + 0x88))(plVar4);
      _ZN8firebase8LogErrorEPKcz
                ("Remote Config: Failed to retrieve %s value from key %s","boolean",param_2);
    }
    (**(code **)(*plVar4 + 0xb8))(plVar4,lVar5);
    if (param_3 != 0) {
      *(bool *)(param_3 + 4) = bVar1;
    }
    bVar1 = cVar2 != '\0' && bVar1;
  }
  return bVar1;
}

~~~
