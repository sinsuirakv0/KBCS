# 00b5cdfc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b5cd34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5cd34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0069.md#compare-2cd166a5bf8e5c24b659e5b02a80b6c8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5ce40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ce40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0070.md#compare-d5eca796477c9d3dcfd14779d519df43)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5cdfc",
  "name": "_ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bfa374a5f8e394be7344b3f1f59b721425b88cbf1f702ddc062c9cd9bbcb27cc",
  "source_text_sha256": "bfa374a5f8e394be7344b3f1f59b721425b88cbf1f702ddc062c9cd9bbcb27cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5cdfc",
        "00b5ce67"
      ]
    ],
    "bytes_sha256": "2a1492d77c87fd5e647995b2349627da9a0406577cc01579d70fd3a3ad822261",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde090](../00bde/00bde090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 493 bytes

~~~c

bool _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_010a1490 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a1488,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_010a1490 = iVar2 == 0;
    bVar1 = (bool)DAT_010a1490;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5cdfc"></a> `00b5cdfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5ce00"></a> `00b5ce00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ce04"></a> `00b5ce04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ce08"></a> `00b5ce08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5ce0c"></a> `00b5ce0c` | `35 2a 00 b0` | adrp x21,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5ce10"></a> `00b5ce10` | `a8 42 52 39` | ldrb w8,[x21, #0x490] | `FALL_THROUGH`
<a id="insn-00b5ce14"></a> `00b5ce14` | `68 00 00 34` | cbz w8,0x00b5ce20 | `CONDITIONAL_JUMP`
<a id="insn-00b5ce18"></a> `00b5ce18` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b5ce1c"></a> `00b5ce1c` | `0f 00 00 14` | b 0x00b5ce58 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5ce20"></a> `00b5ce20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5ce24"></a> `00b5ce24` | `29 2a 00 b0` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5ce28"></a> `00b5ce28` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00b5ce2c"></a> `00b5ce2c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00b5ce30"></a> `00b5ce30` | `21 45 42 f9` | ldr x1,[x9, #0x488] | `FALL_THROUGH`
<a id="insn-00b5ce34"></a> `00b5ce34` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00b5ce38"></a> `00b5ce38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5ce3c"></a> `00b5ce3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5ce40"></a> `00b5ce40` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00b5ce44"></a> `00b5ce44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5ce48"></a> `00b5ce48` | `92 04 02 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b5ce4c"></a> `00b5ce4c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00b5ce50"></a> `00b5ce50` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00b5ce54"></a> `00b5ce54` | `a0 42 12 39` | strb w0,[x21, #0x490] | `FALL_THROUGH`
<a id="insn-00b5ce58"></a> `00b5ce58` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ce5c"></a> `00b5ce5c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5ce60"></a> `00b5ce60` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5ce64"></a> `00b5ce64` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5cdfc`](#insn-00b5cdfc) 範囲 `[['00b5cdfc', '00b5ce17']]`
  - `CONDITIONAL_JUMP` [`00b5ce14`](#insn-00b5ce14) → [`00b5ce20`](#insn-00b5ce20)
  - `FALL_THROUGH` [`00b5ce14`](#insn-00b5ce14) → [`00b5ce18`](#insn-00b5ce18)
- ブロック [`00b5ce18`](#insn-00b5ce18) 範囲 `[['00b5ce18', '00b5ce1f']]`
  - `UNCONDITIONAL_JUMP` [`00b5ce1c`](#insn-00b5ce1c) → [`00b5ce58`](#insn-00b5ce58)
- ブロック [`00b5ce20`](#insn-00b5ce20) 範囲 `[['00b5ce20', '00b5ce57']]`
  - `FALL_THROUGH` [`00b5ce54`](#insn-00b5ce54) → [`00b5ce58`](#insn-00b5ce58)
- ブロック [`00b5ce58`](#insn-00b5ce58) 範囲 `[['00b5ce58', '00b5ce67']]`

## 命令位置別の参照

- [`00b5cdfc`](#insn-00b5cdfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce00`](#insn-00b5ce00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce04`](#insn-00b5ce04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce10`](#insn-00b5ce10) → `010a1490`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b5ce14`](#insn-00b5ce14) → [`00b5ce20`](#insn-00b5ce20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce1c`](#insn-00b5ce1c) → [`00b5ce58`](#insn-00b5ce58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce30`](#insn-00b5ce30) → `010a1488`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ce48`](#insn-00b5ce48) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce54`](#insn-00b5ce54) → `010a1490`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b5ce58`](#insn-00b5ce58) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ce5c`](#insn-00b5ce5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5cdfc`](#insn-00b5cdfc)

~~~json
{
  "source": "00b5cdfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ce00`](#insn-00b5ce00)

~~~json
{
  "source": "00b5ce00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ce04`](#insn-00b5ce04)

~~~json
{
  "source": "00b5ce04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ce10`](#insn-00b5ce10)

~~~json
{
  "source": "00b5ce10",
  "target": "010a1490",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1490",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ce14`](#insn-00b5ce14)

~~~json
{
  "source": "00b5ce14",
  "target": "00b5ce20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ce1c`](#insn-00b5ce1c)

~~~json
{
  "source": "00b5ce1c",
  "target": "00b5ce58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ce30`](#insn-00b5ce30)

~~~json
{
  "source": "00b5ce30",
  "target": "010a1488",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1488",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ce48`](#insn-00b5ce48)

~~~json
{
  "source": "00b5ce48",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5ce54`](#insn-00b5ce54)

~~~json
{
  "source": "00b5ce54",
  "target": "010a1490",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1490",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ce58`](#insn-00b5ce58)

~~~json
{
  "source": "00b5ce58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ce5c`](#insn-00b5ce5c)

~~~json
{
  "source": "00b5ce5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
