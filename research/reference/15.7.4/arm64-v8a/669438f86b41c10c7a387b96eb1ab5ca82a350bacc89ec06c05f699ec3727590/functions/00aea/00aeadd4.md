# 00aeadd4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aead90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-a889ab6a2bbc6b3ae2e898a4d06e64c7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4ab58`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab58.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-1845a3bad0e2d40fd46cb4cb7ede8548)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeadd4",
  "name": "_ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1af9bcab096413634acc8f5ead41b0ddd62ca47a8c4e6383acbcba6ac97f7d1",
  "source_text_sha256": "e1af9bcab096413634acc8f5ead41b0ddd62ca47a8c4e6383acbcba6ac97f7d1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeadd4",
        "00aeae6f"
      ]
    ],
    "bytes_sha256": "a2f7d3daa7083bb2c001d75453712053641878f6e2d86ee35357e561456116fd",
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

## 疑似コード / UTF-8 2215 bytes

~~~c

bool _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0858 == '\0') {
                    /* try { // try from 00aeae0c to 00beb20f has its CatchHandler @ 00aeae0c
                       catch() { ... } // from try @ 00aeae0c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeb3e8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeb554 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aebac8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aec180 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aec4d8 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeca18 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeca9c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aecd6c with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aedb34 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aeed74 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef3fc with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef710 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00aef7e0 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1090 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1410 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1510 with catch @ 00aeae0c
                       catch() { ... } // from try @ 00af1644 with catch @ 00aeae0c */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0850,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0858 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0858;
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
<a id="insn-00aeadd4"></a> `00aeadd4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeadd8"></a> `00aeadd8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaddc"></a> `00aeaddc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeade0"></a> `00aeade0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeade4"></a> `00aeade4` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeade8"></a> `00aeade8` | `a8 62 61 39` | ldrb w8,[x21, #0x858] | `FALL_THROUGH`
<a id="insn-00aeadec"></a> `00aeadec` | `68 00 00 34` | cbz w8,0x00aeadf8 | `CONDITIONAL_JUMP`
<a id="insn-00aeadf0"></a> `00aeadf0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aeadf4"></a> `00aeadf4` | `1b 00 00 14` | b 0x00aeae60 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeadf8"></a> `00aeadf8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeadfc"></a> `00aeadfc` | `a9 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeae00"></a> `00aeae00` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aeae04"></a> `00aeae04` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aeae08"></a> `00aeae08` | `21 29 44 f9` | ldr x1,[x9, #0x850] | `FALL_THROUGH`
<a id="insn-00aeae0c"></a> `00aeae0c` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aeae10"></a> `00aeae10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeae14"></a> `00aeae14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae18"></a> `00aeae18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae1c"></a> `00aeae1c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aeae20"></a> `00aeae20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae24"></a> `00aeae24` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeae28"></a> `00aeae28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae2c"></a> `00aeae2c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeae30"></a> `00aeae30` | `20 01 00 54` | b.eq 0x00aeae54 | `CONDITIONAL_JUMP`
<a id="insn-00aeae34"></a> `00aeae34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae38"></a> `00aeae38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae3c"></a> `00aeae3c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeae40"></a> `00aeae40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae44"></a> `00aeae44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae48"></a> `00aeae48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae4c"></a> `00aeae4c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeae50"></a> `00aeae50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae54"></a> `00aeae54` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aeae58"></a> `00aeae58` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aeae5c"></a> `00aeae5c` | `a0 62 21 39` | strb w0,[x21, #0x858] | `FALL_THROUGH`
<a id="insn-00aeae60"></a> `00aeae60` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeae64"></a> `00aeae64` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeae68"></a> `00aeae68` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeae6c"></a> `00aeae6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeadd4`](#insn-00aeadd4) 範囲 `[['00aeadd4', '00aeadef']]`
  - `CONDITIONAL_JUMP` [`00aeadec`](#insn-00aeadec) → [`00aeadf8`](#insn-00aeadf8)
  - `FALL_THROUGH` [`00aeadec`](#insn-00aeadec) → [`00aeadf0`](#insn-00aeadf0)
- ブロック [`00aeadf0`](#insn-00aeadf0) 範囲 `[['00aeadf0', '00aeadf7']]`
  - `UNCONDITIONAL_JUMP` [`00aeadf4`](#insn-00aeadf4) → [`00aeae60`](#insn-00aeae60)
- ブロック [`00aeadf8`](#insn-00aeadf8) 範囲 `[['00aeadf8', '00aeae0b']]`
  - `FALL_THROUGH` [`00aeae08`](#insn-00aeae08) → [`00aeae0c`](#insn-00aeae0c)
- ブロック [`00aeae0c`](#insn-00aeae0c) 範囲 `[['00aeae0c', '00aeae33']]`
  - `CONDITIONAL_JUMP` [`00aeae30`](#insn-00aeae30) → [`00aeae54`](#insn-00aeae54)
  - `FALL_THROUGH` [`00aeae30`](#insn-00aeae30) → [`00aeae34`](#insn-00aeae34)
- ブロック [`00aeae34`](#insn-00aeae34) 範囲 `[['00aeae34', '00aeae53']]`
  - `FALL_THROUGH` [`00aeae50`](#insn-00aeae50) → [`00aeae54`](#insn-00aeae54)
- ブロック [`00aeae54`](#insn-00aeae54) 範囲 `[['00aeae54', '00aeae5f']]`
  - `FALL_THROUGH` [`00aeae5c`](#insn-00aeae5c) → [`00aeae60`](#insn-00aeae60)
- ブロック [`00aeae60`](#insn-00aeae60) 範囲 `[['00aeae60', '00aeae6f']]`

## 命令位置別の参照

- [`00aeadd4`](#insn-00aeadd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeadd8`](#insn-00aeadd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaddc`](#insn-00aeaddc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeade8`](#insn-00aeade8) → `010a0858`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeadec`](#insn-00aeadec) → [`00aeadf8`](#insn-00aeadf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeadf4`](#insn-00aeadf4) → [`00aeae60`](#insn-00aeae60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae08`](#insn-00aeae08) → `010a0850`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeae30`](#insn-00aeae30) → [`00aeae54`](#insn-00aeae54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae5c`](#insn-00aeae5c) → `010a0858`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeae60`](#insn-00aeae60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae64`](#insn-00aeae64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeadd4`](#insn-00aeadd4)

~~~json
{
  "source": "00aeadd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeadd8`](#insn-00aeadd8)

~~~json
{
  "source": "00aeadd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaddc`](#insn-00aeaddc)

~~~json
{
  "source": "00aeaddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeade8`](#insn-00aeade8)

~~~json
{
  "source": "00aeade8",
  "target": "010a0858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0858",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeadec`](#insn-00aeadec)

~~~json
{
  "source": "00aeadec",
  "target": "00aeadf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeadf4`](#insn-00aeadf4)

~~~json
{
  "source": "00aeadf4",
  "target": "00aeae60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae08`](#insn-00aeae08)

~~~json
{
  "source": "00aeae08",
  "target": "010a0850",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0850",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeae30`](#insn-00aeae30)

~~~json
{
  "source": "00aeae30",
  "target": "00aeae54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae5c`](#insn-00aeae5c)

~~~json
{
  "source": "00aeae5c",
  "target": "010a0858",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0858",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeae60`](#insn-00aeae60)

~~~json
{
  "source": "00aeae60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae64`](#insn-00aeae64)

~~~json
{
  "source": "00aeae64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
