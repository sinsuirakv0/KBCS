# 00aed2bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aed1f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed1f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-37a9a1a2d4a442655e244554cfb52202)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aed300`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aed300.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-40ce7726c056e52bef25630cb654457c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed2bc",
  "name": "_ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "22f9d7c37140469f9c96aa96dc7b88acf920e59fe6b95948dfc041282aff1811",
  "source_text_sha256": "22f9d7c37140469f9c96aa96dc7b88acf920e59fe6b95948dfc041282aff1811",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aed2bc",
        "00aed35b"
      ]
    ],
    "bytes_sha256": "182423d75bf8c20296dedd16df4892b42dfabd78db243b80c4f7ccd175383672",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a09a8 != 0) {
    if (DAT_010a09b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a09b0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a09a8);
    DAT_010a09a8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aed2bc"></a> `00aed2bc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aed2c0"></a> `00aed2c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed2c4"></a> `00aed2c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed2c8"></a> `00aed2c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aed2cc"></a> `00aed2cc` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed2d0"></a> `00aed2d0` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aed2d4"></a> `00aed2d4` | `c1 03 00 b4` | cbz x1,0x00aed34c | `CONDITIONAL_JUMP`
<a id="insn-00aed2d8"></a> `00aed2d8` | `95 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed2dc"></a> `00aed2dc` | `a8 c2 66 39` | ldrb w8,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aed2e0"></a> `00aed2e0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aed2e4"></a> `00aed2e4` | `c8 00 00 34` | cbz w8,0x00aed2fc | `CONDITIONAL_JUMP`
<a id="insn-00aed2e8"></a> `00aed2e8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aed2ec"></a> `00aed2ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed2f0"></a> `00aed2f0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aed2f4"></a> `00aed2f4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aed2f8"></a> `00aed2f8` | `bf c2 26 39` | strb wzr,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00aed2fc"></a> `00aed2fc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aed300"></a> `00aed300` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed304"></a> `00aed304` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aed308"></a> `00aed308` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aed30c"></a> `00aed30c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aed310"></a> `00aed310` | `20 01 00 54` | b.eq 0x00aed334 | `CONDITIONAL_JUMP`
<a id="insn-00aed314"></a> `00aed314` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aed318"></a> `00aed318` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed31c"></a> `00aed31c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aed320"></a> `00aed320` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aed324"></a> `00aed324` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aed328"></a> `00aed328` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed32c"></a> `00aed32c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aed330"></a> `00aed330` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aed334"></a> `00aed334` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aed338"></a> `00aed338` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aed33c"></a> `00aed33c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed340"></a> `00aed340` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aed344"></a> `00aed344` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aed348"></a> `00aed348` | `9f d6 04 f9` | str xzr,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00aed34c"></a> `00aed34c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aed350"></a> `00aed350` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed354"></a> `00aed354` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aed358"></a> `00aed358` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aed2bc`](#insn-00aed2bc) 範囲 `[['00aed2bc', '00aed2d7']]`
  - `CONDITIONAL_JUMP` [`00aed2d4`](#insn-00aed2d4) → [`00aed34c`](#insn-00aed34c)
  - `FALL_THROUGH` [`00aed2d4`](#insn-00aed2d4) → [`00aed2d8`](#insn-00aed2d8)
- ブロック [`00aed2d8`](#insn-00aed2d8) 範囲 `[['00aed2d8', '00aed2e7']]`
  - `CONDITIONAL_JUMP` [`00aed2e4`](#insn-00aed2e4) → [`00aed2fc`](#insn-00aed2fc)
  - `FALL_THROUGH` [`00aed2e4`](#insn-00aed2e4) → [`00aed2e8`](#insn-00aed2e8)
- ブロック [`00aed2e8`](#insn-00aed2e8) 範囲 `[['00aed2e8', '00aed2fb']]`
  - `FALL_THROUGH` [`00aed2f8`](#insn-00aed2f8) → [`00aed2fc`](#insn-00aed2fc)
- ブロック [`00aed2fc`](#insn-00aed2fc) 範囲 `[['00aed2fc', '00aed313']]`
  - `CONDITIONAL_JUMP` [`00aed310`](#insn-00aed310) → [`00aed334`](#insn-00aed334)
  - `FALL_THROUGH` [`00aed310`](#insn-00aed310) → [`00aed314`](#insn-00aed314)
- ブロック [`00aed314`](#insn-00aed314) 範囲 `[['00aed314', '00aed333']]`
  - `FALL_THROUGH` [`00aed330`](#insn-00aed330) → [`00aed334`](#insn-00aed334)
- ブロック [`00aed334`](#insn-00aed334) 範囲 `[['00aed334', '00aed34b']]`
  - `FALL_THROUGH` [`00aed348`](#insn-00aed348) → [`00aed34c`](#insn-00aed34c)
- ブロック [`00aed34c`](#insn-00aed34c) 範囲 `[['00aed34c', '00aed35b']]`

## 命令位置別の参照

- [`00aed2bc`](#insn-00aed2bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed2c0`](#insn-00aed2c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed2c4`](#insn-00aed2c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed2d0`](#insn-00aed2d0) → `010a09a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed2d4`](#insn-00aed2d4) → [`00aed34c`](#insn-00aed34c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed2dc`](#insn-00aed2dc) → `010a09b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aed2e4`](#insn-00aed2e4) → [`00aed2fc`](#insn-00aed2fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed2f8`](#insn-00aed2f8) → `010a09b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aed310`](#insn-00aed310) → [`00aed334`](#insn-00aed334) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed338`](#insn-00aed338) → `010a09a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed348`](#insn-00aed348) → `010a09a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed34c`](#insn-00aed34c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed350`](#insn-00aed350) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aed2bc`](#insn-00aed2bc)

~~~json
{
  "source": "00aed2bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed2c0`](#insn-00aed2c0)

~~~json
{
  "source": "00aed2c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed2c4`](#insn-00aed2c4)

~~~json
{
  "source": "00aed2c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed2d0`](#insn-00aed2d0)

~~~json
{
  "source": "00aed2d0",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed2d4`](#insn-00aed2d4)

~~~json
{
  "source": "00aed2d4",
  "target": "00aed34c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed2dc`](#insn-00aed2dc)

~~~json
{
  "source": "00aed2dc",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed2e4`](#insn-00aed2e4)

~~~json
{
  "source": "00aed2e4",
  "target": "00aed2fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed2f8`](#insn-00aed2f8)

~~~json
{
  "source": "00aed2f8",
  "target": "010a09b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed310`](#insn-00aed310)

~~~json
{
  "source": "00aed310",
  "target": "00aed334",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed338`](#insn-00aed338)

~~~json
{
  "source": "00aed338",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed348`](#insn-00aed348)

~~~json
{
  "source": "00aed348",
  "target": "010a09a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed34c`](#insn-00aed34c)

~~~json
{
  "source": "00aed34c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed350`](#insn-00aed350)

~~~json
{
  "source": "00aed350",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
