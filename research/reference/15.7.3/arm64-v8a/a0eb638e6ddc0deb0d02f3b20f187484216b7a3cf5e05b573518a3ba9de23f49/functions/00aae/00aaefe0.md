# 00aaefe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00aaefe0",
  "name": "FUN_00aaefe0",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d281ff9a589ccf98e41925a244b053bc616ab61a63222b33d3d81b3a463c65f5",
  "source_text_sha256": "d281ff9a589ccf98e41925a244b053bc616ab61a63222b33d3d81b3a463c65f5"
}
~~~

## 呼び出し元

- [009c5338](../009c5/009c5338.md)

## 呼び出し先

- [0045de70](../0045d/0045de70.md)
- [0045df50](../0045d/0045df50.md)

## 疑似コード / UTF-8 696 bytes

~~~c

void FUN_00aaefe0(undefined4 *param_1,undefined8 param_2)

{
  FUN_0045df50(param_2,*param_1);
  FUN_0045df50(param_2,param_1[3]);
  FUN_0045df50(param_2,param_1[5]);
  FUN_0045df50(param_2,param_1[4]);
  FUN_0045df50(param_2,param_1[1]);
  FUN_0045df50(param_2,*(undefined1 *)(param_1 + 7));
  FUN_0045df50(param_2,*(undefined1 *)((long)param_1 + 0x1d));
  FUN_0045df50(param_2,*(undefined1 *)((long)param_1 + 0x1e));
  FUN_0045df50(param_2,*(undefined1 *)((long)param_1 + 0x1f));
  FUN_0045df50(param_2,param_1[2]);
  FUN_0045df50(param_2,*(undefined1 *)(param_1 + 8));
  FUN_0045df50(param_2,*(undefined1 *)(param_1 + 9));
  FUN_0045de70(param_2,*(undefined1 *)(param_1 + 0xb));
  return;
}

~~~
