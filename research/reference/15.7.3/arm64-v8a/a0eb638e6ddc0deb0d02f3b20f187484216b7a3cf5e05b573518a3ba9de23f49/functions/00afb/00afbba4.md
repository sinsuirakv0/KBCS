# 00afbba4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afbadc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbadc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-f29036221751e5c89086e4e0968702ab)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afbbe8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbbe8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-be19faf2c45f0efaa56d5d84959d4da0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbba4",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dbd6d642174386cc5168a210f0d0a0c753e24a59318cfb949d0041beea435a41",
  "source_text_sha256": "dbd6d642174386cc5168a210f0d0a0c753e24a59318cfb949d0041beea435a41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbba4",
        "00afbc2b"
      ]
    ],
    "bytes_sha256": "dfb2c8bd61dd533e0d56e311235baacc2672fc4bad6c98237d0d78c92f519b2c",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb780](../00bdb/00bdb780.md)
- [00bdebe0](../00bde/00bdebe0.md)
- [00bdec40](../00bde/00bdec40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0cf8 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbbcc to 00bfbbd3 has its CatchHandler @ 00aff418 */
    if ((__thread1 == 0) || (DAT_010a0d00 == 0)) {
      if (DAT_010a0d00 != 0 || __thread1 != 0) goto LAB_00afbc1c;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0d00);
      if (iVar1 == 0) goto LAB_00afbc1c;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbbfc to 00bfbc13 has its CatchHandler @ 00aff414 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbc1c:
                    /* try { // try from 00afbc24 to 00bfbc3b has its CatchHandler @ 00b0037c */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbba4"></a> `00afbba4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afbba8"></a> `00afbba8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbbac"></a> `00afbbac` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00afbbb0"></a> `00afbbb0` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbbb4"></a> `00afbbb4` | `08 e1 73 39` | ldrb w8,[x8, #0xcf8] | `FALL_THROUGH`
<a id="insn-00afbbb8"></a> `00afbbb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbbbc"></a> `00afbbbc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbbc0"></a> `00afbbc0` | `e1 02 00 54` | b.ne 0x00afbc1c | `CONDITIONAL_JUMP`
<a id="insn-00afbbc4"></a> `00afbbc4` | `ef 7e 03 94` | bl 0x00bdb780 | `UNCONDITIONAL_CALL`
<a id="insn-00afbbc8"></a> `00afbbc8` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbbcc"></a> `00afbbcc` | `01 81 46 f9` | ldr x1,[x8, #0xd00] | `FALL_THROUGH`
<a id="insn-00afbbd0"></a> `00afbbd0` | `20 02 00 b4` | cbz x0,0x00afbc14 | `CONDITIONAL_JUMP`
<a id="insn-00afbbd4"></a> `00afbbd4` | `01 02 00 b4` | cbz x1,0x00afbc14 | `CONDITIONAL_JUMP`
<a id="insn-00afbbd8"></a> `00afbbd8` | `1a 8c 03 94` | bl 0x00bdec40 | `UNCONDITIONAL_CALL`
<a id="insn-00afbbdc"></a> `00afbbdc` | `00 02 00 34` | cbz w0,0x00afbc1c | `CONDITIONAL_JUMP`
<a id="insn-00afbbe0"></a> `00afbbe0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbbe4"></a> `00afbbe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbbe8"></a> `00afbbe8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbbec"></a> `00afbbec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbbf0"></a> `00afbbf0` | `b3 00 00 b4` | cbz x19,0x00afbc04 | `CONDITIONAL_JUMP`
<a id="insn-00afbbf4"></a> `00afbbf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbbf8"></a> `00afbbf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbbfc"></a> `00afbbfc` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afbc00"></a> `00afbc00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbc04"></a> `00afbc04` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbc08"></a> `00afbc08` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00afbc0c"></a> `00afbc0c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbc10"></a> `00afbc10` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afbc14"></a> `00afbc14` | `28 00 00 aa` | orr x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00afbc18"></a> `00afbc18` | `48 fe ff b4` | cbz x8,0x00afbbe0 | `CONDITIONAL_JUMP`
<a id="insn-00afbc1c"></a> `00afbc1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbc20"></a> `00afbc20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbc24"></a> `00afbc24` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afbc28"></a> `00afbc28` | `ee 8b 03 14` | b 0x00bdebe0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbba4`](#insn-00afbba4) 範囲 `[['00afbba4', '00afbbc3']]`
  - `CONDITIONAL_JUMP` [`00afbbc0`](#insn-00afbbc0) → [`00afbc1c`](#insn-00afbc1c)
  - `FALL_THROUGH` [`00afbbc0`](#insn-00afbbc0) → [`00afbbc4`](#insn-00afbbc4)
- ブロック [`00afbbc4`](#insn-00afbbc4) 範囲 `[['00afbbc4', '00afbbcb']]`
  - `FALL_THROUGH` [`00afbbc8`](#insn-00afbbc8) → [`00afbbcc`](#insn-00afbbcc)
- ブロック [`00afbbcc`](#insn-00afbbcc) 範囲 `[['00afbbcc', '00afbbd3']]`
  - `CONDITIONAL_JUMP` [`00afbbd0`](#insn-00afbbd0) → [`00afbc14`](#insn-00afbc14)
  - `FALL_THROUGH` [`00afbbd0`](#insn-00afbbd0) → [`00afbbd4`](#insn-00afbbd4)
- ブロック [`00afbbd4`](#insn-00afbbd4) 範囲 `[['00afbbd4', '00afbbd7']]`
  - `CONDITIONAL_JUMP` [`00afbbd4`](#insn-00afbbd4) → [`00afbc14`](#insn-00afbc14)
  - `FALL_THROUGH` [`00afbbd4`](#insn-00afbbd4) → [`00afbbd8`](#insn-00afbbd8)
- ブロック [`00afbbd8`](#insn-00afbbd8) 範囲 `[['00afbbd8', '00afbbdf']]`
  - `CONDITIONAL_JUMP` [`00afbbdc`](#insn-00afbbdc) → [`00afbc1c`](#insn-00afbc1c)
  - `FALL_THROUGH` [`00afbbdc`](#insn-00afbbdc) → [`00afbbe0`](#insn-00afbbe0)
- ブロック [`00afbbe0`](#insn-00afbbe0) 範囲 `[['00afbbe0', '00afbbf3']]`
  - `CONDITIONAL_JUMP` [`00afbbf0`](#insn-00afbbf0) → [`00afbc04`](#insn-00afbc04)
  - `FALL_THROUGH` [`00afbbf0`](#insn-00afbbf0) → [`00afbbf4`](#insn-00afbbf4)
- ブロック [`00afbbf4`](#insn-00afbbf4) 範囲 `[['00afbbf4', '00afbbfb']]`
  - `FALL_THROUGH` [`00afbbf8`](#insn-00afbbf8) → [`00afbbfc`](#insn-00afbbfc)
- ブロック [`00afbbfc`](#insn-00afbbfc) 範囲 `[['00afbbfc', '00afbc03']]`
  - `FALL_THROUGH` [`00afbc00`](#insn-00afbc00) → [`00afbc04`](#insn-00afbc04)
- ブロック [`00afbc04`](#insn-00afbc04) 範囲 `[['00afbc04', '00afbc13']]`
- ブロック [`00afbc14`](#insn-00afbc14) 範囲 `[['00afbc14', '00afbc1b']]`
  - `CONDITIONAL_JUMP` [`00afbc18`](#insn-00afbc18) → [`00afbbe0`](#insn-00afbbe0)
  - `FALL_THROUGH` [`00afbc18`](#insn-00afbc18) → [`00afbc1c`](#insn-00afbc1c)
- ブロック [`00afbc1c`](#insn-00afbc1c) 範囲 `[['00afbc1c', '00afbc23']]`
  - `FALL_THROUGH` [`00afbc20`](#insn-00afbc20) → [`00afbc24`](#insn-00afbc24)
- ブロック [`00afbc24`](#insn-00afbc24) 範囲 `[['00afbc24', '00afbc2b']]`

## 命令位置別の参照

- [`00afbba4`](#insn-00afbba4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbba8`](#insn-00afbba8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbb4`](#insn-00afbbb4) → `010a0cf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00afbbc0`](#insn-00afbbc0) → [`00afbc1c`](#insn-00afbc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbc4`](#insn-00afbbc4) → [`00bdb780`](../00bdb/00bdb780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb780` · 推定シンボル `None` · 推定型 `None`
- [`00afbbcc`](#insn-00afbbcc) → `010a0d00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbbd0`](#insn-00afbbd0) → [`00afbc14`](#insn-00afbc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbd4`](#insn-00afbbd4) → [`00afbc14`](#insn-00afbc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbd8`](#insn-00afbbd8) → [`00bdec40`](../00bde/00bdec40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec40` · 推定シンボル `None` · 推定型 `None`
- [`00afbbdc`](#insn-00afbbdc) → [`00afbc1c`](#insn-00afbc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbbf0`](#insn-00afbbf0) → [`00afbc04`](#insn-00afbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc04`](#insn-00afbc04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc18`](#insn-00afbc18) → [`00afbbe0`](#insn-00afbbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc1c`](#insn-00afbc1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc28`](#insn-00afbc28) → [`00bdebe0`](../00bde/00bdebe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdebe0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbba4`](#insn-00afbba4)

~~~json
{
  "source": "00afbba4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbba8`](#insn-00afbba8)

~~~json
{
  "source": "00afbba8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbb4`](#insn-00afbbb4)

~~~json
{
  "source": "00afbbb4",
  "target": "010a0cf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0cf8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbbc0`](#insn-00afbbc0)

~~~json
{
  "source": "00afbbc0",
  "target": "00afbc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbc4`](#insn-00afbbc4)

~~~json
{
  "source": "00afbbc4",
  "target": "00bdb780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbbcc`](#insn-00afbbcc)

~~~json
{
  "source": "00afbbcc",
  "target": "010a0d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbbd0`](#insn-00afbbd0)

~~~json
{
  "source": "00afbbd0",
  "target": "00afbc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbd4`](#insn-00afbbd4)

~~~json
{
  "source": "00afbbd4",
  "target": "00afbc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbd8`](#insn-00afbbd8)

~~~json
{
  "source": "00afbbd8",
  "target": "00bdec40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbbdc`](#insn-00afbbdc)

~~~json
{
  "source": "00afbbdc",
  "target": "00afbc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbbf0`](#insn-00afbbf0)

~~~json
{
  "source": "00afbbf0",
  "target": "00afbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc04`](#insn-00afbc04)

~~~json
{
  "source": "00afbc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc18`](#insn-00afbc18)

~~~json
{
  "source": "00afbc18",
  "target": "00afbbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc1c`](#insn-00afbc1c)

~~~json
{
  "source": "00afbc1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc28`](#insn-00afbc28)

~~~json
{
  "source": "00afbc28",
  "target": "00bdebe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
