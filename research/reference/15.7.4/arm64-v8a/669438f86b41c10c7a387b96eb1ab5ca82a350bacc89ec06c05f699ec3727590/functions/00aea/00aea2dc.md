# 00aea2dc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aea298`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea298.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-3646d3dde5f95dac37f390f14266d9f7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4a060`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0057.md#compare-b5bcdb2578c32b98eb5a58f42a8b783b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aea2dc",
  "name": "_ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc4becfe89ac7cf1498e5bc744af806fbc19564d359670d1a9a13a242bcad376",
  "source_text_sha256": "cc4becfe89ac7cf1498e5bc744af806fbc19564d359670d1a9a13a242bcad376",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aea2dc",
        "00aea377"
      ]
    ],
    "bytes_sha256": "9fc26fb7f0db6f416e686e5d1914360d98b7f4d5ec6cc86179709ad57ca0a77e",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 609 bytes

~~~c

bool _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a07b0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a07a8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a07b0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a07b0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aea2dc"></a> `00aea2dc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aea2e0"></a> `00aea2e0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea2e4"></a> `00aea2e4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea2e8"></a> `00aea2e8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aea2ec"></a> `00aea2ec` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea2f0"></a> `00aea2f0` | `a8 c2 5e 39` | ldrb w8,[x21, #0x7b0] | `FALL_THROUGH`
<a id="insn-00aea2f4"></a> `00aea2f4` | `68 00 00 34` | cbz w8,0x00aea300 | `CONDITIONAL_JUMP`
<a id="insn-00aea2f8"></a> `00aea2f8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aea2fc"></a> `00aea2fc` | `1b 00 00 14` | b 0x00aea368 | `UNCONDITIONAL_JUMP`
<a id="insn-00aea300"></a> `00aea300` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aea304"></a> `00aea304` | `a9 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aea308"></a> `00aea308` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aea30c"></a> `00aea30c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aea310"></a> `00aea310` | `21 d5 43 f9` | ldr x1,[x9, #0x7a8] | `FALL_THROUGH`
<a id="insn-00aea314"></a> `00aea314` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aea318"></a> `00aea318` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aea31c"></a> `00aea31c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea320"></a> `00aea320` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea324"></a> `00aea324` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aea328"></a> `00aea328` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea32c"></a> `00aea32c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aea330"></a> `00aea330` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea334"></a> `00aea334` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aea338"></a> `00aea338` | `20 01 00 54` | b.eq 0x00aea35c | `CONDITIONAL_JUMP`
<a id="insn-00aea33c"></a> `00aea33c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea340"></a> `00aea340` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea344"></a> `00aea344` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aea348"></a> `00aea348` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea34c"></a> `00aea34c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aea350"></a> `00aea350` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aea354"></a> `00aea354` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aea358"></a> `00aea358` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aea35c"></a> `00aea35c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aea360"></a> `00aea360` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aea364"></a> `00aea364` | `a0 c2 1e 39` | strb w0,[x21, #0x7b0] | `FALL_THROUGH`
<a id="insn-00aea368"></a> `00aea368` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aea36c"></a> `00aea36c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aea370"></a> `00aea370` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aea374"></a> `00aea374` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aea2dc`](#insn-00aea2dc) 範囲 `[['00aea2dc', '00aea2f7']]`
  - `CONDITIONAL_JUMP` [`00aea2f4`](#insn-00aea2f4) → [`00aea300`](#insn-00aea300)
  - `FALL_THROUGH` [`00aea2f4`](#insn-00aea2f4) → [`00aea2f8`](#insn-00aea2f8)
- ブロック [`00aea2f8`](#insn-00aea2f8) 範囲 `[['00aea2f8', '00aea2ff']]`
  - `UNCONDITIONAL_JUMP` [`00aea2fc`](#insn-00aea2fc) → [`00aea368`](#insn-00aea368)
- ブロック [`00aea300`](#insn-00aea300) 範囲 `[['00aea300', '00aea33b']]`
  - `CONDITIONAL_JUMP` [`00aea338`](#insn-00aea338) → [`00aea35c`](#insn-00aea35c)
  - `FALL_THROUGH` [`00aea338`](#insn-00aea338) → [`00aea33c`](#insn-00aea33c)
- ブロック [`00aea33c`](#insn-00aea33c) 範囲 `[['00aea33c', '00aea35b']]`
  - `FALL_THROUGH` [`00aea358`](#insn-00aea358) → [`00aea35c`](#insn-00aea35c)
- ブロック [`00aea35c`](#insn-00aea35c) 範囲 `[['00aea35c', '00aea367']]`
  - `FALL_THROUGH` [`00aea364`](#insn-00aea364) → [`00aea368`](#insn-00aea368)
- ブロック [`00aea368`](#insn-00aea368) 範囲 `[['00aea368', '00aea377']]`

## 命令位置別の参照

- [`00aea2dc`](#insn-00aea2dc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea2e0`](#insn-00aea2e0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea2e4`](#insn-00aea2e4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea2f0`](#insn-00aea2f0) → `010a07b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aea2f4`](#insn-00aea2f4) → [`00aea300`](#insn-00aea300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea2fc`](#insn-00aea2fc) → [`00aea368`](#insn-00aea368) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea310`](#insn-00aea310) → `010a07a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aea338`](#insn-00aea338) → [`00aea35c`](#insn-00aea35c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea364`](#insn-00aea364) → `010a07b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aea368`](#insn-00aea368) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aea36c`](#insn-00aea36c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aea2dc`](#insn-00aea2dc)

~~~json
{
  "source": "00aea2dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea2e0`](#insn-00aea2e0)

~~~json
{
  "source": "00aea2e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea2e4`](#insn-00aea2e4)

~~~json
{
  "source": "00aea2e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea2f0`](#insn-00aea2f0)

~~~json
{
  "source": "00aea2f0",
  "target": "010a07b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea2f4`](#insn-00aea2f4)

~~~json
{
  "source": "00aea2f4",
  "target": "00aea300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea2fc`](#insn-00aea2fc)

~~~json
{
  "source": "00aea2fc",
  "target": "00aea368",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea310`](#insn-00aea310)

~~~json
{
  "source": "00aea310",
  "target": "010a07a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea338`](#insn-00aea338)

~~~json
{
  "source": "00aea338",
  "target": "00aea35c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea364`](#insn-00aea364)

~~~json
{
  "source": "00aea364",
  "target": "010a07b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aea368`](#insn-00aea368)

~~~json
{
  "source": "00aea368",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aea36c`](#insn-00aea36c)

~~~json
{
  "source": "00aea36c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
