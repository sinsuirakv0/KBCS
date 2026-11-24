# 00aeb8cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeb888`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb888.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-352670b78f185ba8fcc1129b79b64cd5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4b650`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b650.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-16ae94e79c43c191bca23b6e80a4bb80)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeb8cc",
  "name": "_ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dd3014b2534baed86d377b1f12d344e98597ba94d41b84e021772871e82af117",
  "source_text_sha256": "dd3014b2534baed86d377b1f12d344e98597ba94d41b84e021772871e82af117",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeb8cc",
        "00aeb967"
      ]
    ],
    "bytes_sha256": "507cd24a774a1b65c23f8d26455df24b073ca37c1514d8d7f4ff2efdc4895ff1",
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

## 疑似コード / UTF-8 800 bytes

~~~c

bool _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a08e0 == '\0') {
                    /* try { // try from 00aeb90c to 00beb913 has its CatchHandler @ 00af1928 */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a08d8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a08e0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a08e0;
  }
  else {
    bVar2 = false;
  }
                    /* try { // try from 00aeb958 to 00beb96f has its CatchHandler @ 00af1924 */
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeb8cc"></a> `00aeb8cc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeb8d0"></a> `00aeb8d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb8d4"></a> `00aeb8d4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeb8d8"></a> `00aeb8d8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeb8dc"></a> `00aeb8dc` | `b5 2d 00 b0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb8e0"></a> `00aeb8e0` | `a8 82 63 39` | ldrb w8,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00aeb8e4"></a> `00aeb8e4` | `68 00 00 34` | cbz w8,0x00aeb8f0 | `CONDITIONAL_JUMP`
<a id="insn-00aeb8e8"></a> `00aeb8e8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aeb8ec"></a> `00aeb8ec` | `1b 00 00 14` | b 0x00aeb958 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeb8f0"></a> `00aeb8f0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeb8f4"></a> `00aeb8f4` | `a9 2d 00 b0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb8f8"></a> `00aeb8f8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aeb8fc"></a> `00aeb8fc` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aeb900"></a> `00aeb900` | `21 6d 44 f9` | ldr x1,[x9, #0x8d8] | `FALL_THROUGH`
<a id="insn-00aeb904"></a> `00aeb904` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aeb908"></a> `00aeb908` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeb90c"></a> `00aeb90c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeb910"></a> `00aeb910` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeb914"></a> `00aeb914` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aeb918"></a> `00aeb918` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb91c"></a> `00aeb91c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeb920"></a> `00aeb920` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeb924"></a> `00aeb924` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeb928"></a> `00aeb928` | `20 01 00 54` | b.eq 0x00aeb94c | `CONDITIONAL_JUMP`
<a id="insn-00aeb92c"></a> `00aeb92c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeb930"></a> `00aeb930` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb934"></a> `00aeb934` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeb938"></a> `00aeb938` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeb93c"></a> `00aeb93c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeb940"></a> `00aeb940` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeb944"></a> `00aeb944` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeb948"></a> `00aeb948` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeb94c"></a> `00aeb94c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aeb950"></a> `00aeb950` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aeb954"></a> `00aeb954` | `a0 82 23 39` | strb w0,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00aeb958"></a> `00aeb958` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeb95c"></a> `00aeb95c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb960"></a> `00aeb960` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeb964"></a> `00aeb964` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeb8cc`](#insn-00aeb8cc) 範囲 `[['00aeb8cc', '00aeb8e7']]`
  - `CONDITIONAL_JUMP` [`00aeb8e4`](#insn-00aeb8e4) → [`00aeb8f0`](#insn-00aeb8f0)
  - `FALL_THROUGH` [`00aeb8e4`](#insn-00aeb8e4) → [`00aeb8e8`](#insn-00aeb8e8)
- ブロック [`00aeb8e8`](#insn-00aeb8e8) 範囲 `[['00aeb8e8', '00aeb8ef']]`
  - `UNCONDITIONAL_JUMP` [`00aeb8ec`](#insn-00aeb8ec) → [`00aeb958`](#insn-00aeb958)
- ブロック [`00aeb8f0`](#insn-00aeb8f0) 範囲 `[['00aeb8f0', '00aeb90b']]`
  - `FALL_THROUGH` [`00aeb908`](#insn-00aeb908) → [`00aeb90c`](#insn-00aeb90c)
- ブロック [`00aeb90c`](#insn-00aeb90c) 範囲 `[['00aeb90c', '00aeb92b']]`
  - `CONDITIONAL_JUMP` [`00aeb928`](#insn-00aeb928) → [`00aeb94c`](#insn-00aeb94c)
  - `FALL_THROUGH` [`00aeb928`](#insn-00aeb928) → [`00aeb92c`](#insn-00aeb92c)
- ブロック [`00aeb92c`](#insn-00aeb92c) 範囲 `[['00aeb92c', '00aeb94b']]`
  - `FALL_THROUGH` [`00aeb948`](#insn-00aeb948) → [`00aeb94c`](#insn-00aeb94c)
- ブロック [`00aeb94c`](#insn-00aeb94c) 範囲 `[['00aeb94c', '00aeb957']]`
  - `FALL_THROUGH` [`00aeb954`](#insn-00aeb954) → [`00aeb958`](#insn-00aeb958)
- ブロック [`00aeb958`](#insn-00aeb958) 範囲 `[['00aeb958', '00aeb967']]`

## 命令位置別の参照

- [`00aeb8cc`](#insn-00aeb8cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb8d0`](#insn-00aeb8d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb8d4`](#insn-00aeb8d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb8e0`](#insn-00aeb8e0) → `010a08e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeb8e4`](#insn-00aeb8e4) → [`00aeb8f0`](#insn-00aeb8f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb8ec`](#insn-00aeb8ec) → [`00aeb958`](#insn-00aeb958) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb900`](#insn-00aeb900) → `010a08d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeb928`](#insn-00aeb928) → [`00aeb94c`](#insn-00aeb94c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb954`](#insn-00aeb954) → `010a08e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeb958`](#insn-00aeb958) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb95c`](#insn-00aeb95c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeb8cc`](#insn-00aeb8cc)

~~~json
{
  "source": "00aeb8cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb8d0`](#insn-00aeb8d0)

~~~json
{
  "source": "00aeb8d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb8d4`](#insn-00aeb8d4)

~~~json
{
  "source": "00aeb8d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb8e0`](#insn-00aeb8e0)

~~~json
{
  "source": "00aeb8e0",
  "target": "010a08e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb8e4`](#insn-00aeb8e4)

~~~json
{
  "source": "00aeb8e4",
  "target": "00aeb8f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb8ec`](#insn-00aeb8ec)

~~~json
{
  "source": "00aeb8ec",
  "target": "00aeb958",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb900`](#insn-00aeb900)

~~~json
{
  "source": "00aeb900",
  "target": "010a08d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb928`](#insn-00aeb928)

~~~json
{
  "source": "00aeb928",
  "target": "00aeb94c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb954`](#insn-00aeb954)

~~~json
{
  "source": "00aeb954",
  "target": "010a08e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeb958`](#insn-00aeb958)

~~~json
{
  "source": "00aeb958",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb95c`](#insn-00aeb95c)

~~~json
{
  "source": "00aeb95c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
