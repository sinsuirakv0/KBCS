# 00bbbbac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bbbbac",
  "name": "_ZN8firebase9messaging27IsRegistrationOnInitEnabledEv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "341bdc6da625b0e4790802aafb56753c3c77ec0ff56c0c868ffb25920accfcbc",
  "source_text_sha256": "341bdc6da625b0e4790802aafb56753c3c77ec0ff56c0c868ffb25920accfcbc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a08](../00497/00497a08.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 539 bytes

~~~c

bool _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01125f60 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
                    /* try { // try from 00bbbbd0 to 00cbbc6f has its CatchHandler @ 00bbc5cc */
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    if (DAT_01125f60 == 0) {
      return true;
    }
  }
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
  cVar1 = FUN_00497a08(uVar2,DAT_01125f98,DAT_01125eb8);
  return cVar1 != '\0';
}

~~~
