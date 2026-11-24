# 00aeaa2c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aea9e8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea9e8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b369bc3b780d59169bdcd4a4ba9f4a34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4a7b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a7b0.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-0688458f327ce364d8eaf631df2df48b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaa2c",
  "name": "_ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4919c8926ac8f0c34001fcd5c683012eb1645baa0371253e1c4f59a9f547259b",
  "source_text_sha256": "4919c8926ac8f0c34001fcd5c683012eb1645baa0371253e1c4f59a9f547259b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaa2c",
        "00aeaac7"
      ]
    ],
    "bytes_sha256": "c6e826ecfc032c9ac3d7d390a486905080caff2b0d34f1819b0e7d1e8b04d7eb",
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

## 疑似コード / UTF-8 697 bytes

~~~c

bool _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0830 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0828,param_2,param_3);
                    /* catch() { ... } // from try @ 00aeac58 with catch @ 00aeaa7c */
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0830 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0830;
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
<a id="insn-00aeaa2c"></a> `00aeaa2c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeaa30"></a> `00aeaa30` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaa34"></a> `00aeaa34` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaa38"></a> `00aeaa38` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeaa3c"></a> `00aeaa3c` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaa40"></a> `00aeaa40` | `a8 c2 60 39` | ldrb w8,[x21, #0x830] | `FALL_THROUGH`
<a id="insn-00aeaa44"></a> `00aeaa44` | `68 00 00 34` | cbz w8,0x00aeaa50 | `CONDITIONAL_JUMP`
<a id="insn-00aeaa48"></a> `00aeaa48` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aeaa4c"></a> `00aeaa4c` | `1b 00 00 14` | b 0x00aeaab8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeaa50"></a> `00aeaa50` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeaa54"></a> `00aeaa54` | `a9 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaa58"></a> `00aeaa58` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aeaa5c"></a> `00aeaa5c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aeaa60"></a> `00aeaa60` | `21 15 44 f9` | ldr x1,[x9, #0x828] | `FALL_THROUGH`
<a id="insn-00aeaa64"></a> `00aeaa64` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aeaa68"></a> `00aeaa68` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeaa6c"></a> `00aeaa6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa70"></a> `00aeaa70` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaa74"></a> `00aeaa74` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aeaa78"></a> `00aeaa78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa7c"></a> `00aeaa7c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeaa80"></a> `00aeaa80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa84"></a> `00aeaa84` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeaa88"></a> `00aeaa88` | `20 01 00 54` | b.eq 0x00aeaaac | `CONDITIONAL_JUMP`
<a id="insn-00aeaa8c"></a> `00aeaa8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaa90"></a> `00aeaa90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaa94"></a> `00aeaa94` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeaa98"></a> `00aeaa98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaa9c"></a> `00aeaa9c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaaa0"></a> `00aeaaa0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaaa4"></a> `00aeaaa4` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeaaa8"></a> `00aeaaa8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaaac"></a> `00aeaaac` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aeaab0"></a> `00aeaab0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aeaab4"></a> `00aeaab4` | `a0 c2 20 39` | strb w0,[x21, #0x830] | `FALL_THROUGH`
<a id="insn-00aeaab8"></a> `00aeaab8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaabc"></a> `00aeaabc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaac0"></a> `00aeaac0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeaac4"></a> `00aeaac4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaa2c`](#insn-00aeaa2c) 範囲 `[['00aeaa2c', '00aeaa47']]`
  - `CONDITIONAL_JUMP` [`00aeaa44`](#insn-00aeaa44) → [`00aeaa50`](#insn-00aeaa50)
  - `FALL_THROUGH` [`00aeaa44`](#insn-00aeaa44) → [`00aeaa48`](#insn-00aeaa48)
- ブロック [`00aeaa48`](#insn-00aeaa48) 範囲 `[['00aeaa48', '00aeaa4f']]`
  - `UNCONDITIONAL_JUMP` [`00aeaa4c`](#insn-00aeaa4c) → [`00aeaab8`](#insn-00aeaab8)
- ブロック [`00aeaa50`](#insn-00aeaa50) 範囲 `[['00aeaa50', '00aeaa7b']]`
  - `FALL_THROUGH` [`00aeaa78`](#insn-00aeaa78) → [`00aeaa7c`](#insn-00aeaa7c)
- ブロック [`00aeaa7c`](#insn-00aeaa7c) 範囲 `[['00aeaa7c', '00aeaa8b']]`
  - `CONDITIONAL_JUMP` [`00aeaa88`](#insn-00aeaa88) → [`00aeaaac`](#insn-00aeaaac)
  - `FALL_THROUGH` [`00aeaa88`](#insn-00aeaa88) → [`00aeaa8c`](#insn-00aeaa8c)
- ブロック [`00aeaa8c`](#insn-00aeaa8c) 範囲 `[['00aeaa8c', '00aeaaab']]`
  - `FALL_THROUGH` [`00aeaaa8`](#insn-00aeaaa8) → [`00aeaaac`](#insn-00aeaaac)
- ブロック [`00aeaaac`](#insn-00aeaaac) 範囲 `[['00aeaaac', '00aeaab7']]`
  - `FALL_THROUGH` [`00aeaab4`](#insn-00aeaab4) → [`00aeaab8`](#insn-00aeaab8)
- ブロック [`00aeaab8`](#insn-00aeaab8) 範囲 `[['00aeaab8', '00aeaac7']]`

## 命令位置別の参照

- [`00aeaa2c`](#insn-00aeaa2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa30`](#insn-00aeaa30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa34`](#insn-00aeaa34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa40`](#insn-00aeaa40) → `010a0830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeaa44`](#insn-00aeaa44) → [`00aeaa50`](#insn-00aeaa50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa4c`](#insn-00aeaa4c) → [`00aeaab8`](#insn-00aeaab8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaa60`](#insn-00aeaa60) → `010a0828`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaa88`](#insn-00aeaa88) → [`00aeaaac`](#insn-00aeaaac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaab4`](#insn-00aeaab4) → `010a0830`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeaab8`](#insn-00aeaab8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaabc`](#insn-00aeaabc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaa2c`](#insn-00aeaa2c)

~~~json
{
  "source": "00aeaa2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa30`](#insn-00aeaa30)

~~~json
{
  "source": "00aeaa30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa34`](#insn-00aeaa34)

~~~json
{
  "source": "00aeaa34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa40`](#insn-00aeaa40)

~~~json
{
  "source": "00aeaa40",
  "target": "010a0830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0830",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa44`](#insn-00aeaa44)

~~~json
{
  "source": "00aeaa44",
  "target": "00aeaa50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa4c`](#insn-00aeaa4c)

~~~json
{
  "source": "00aeaa4c",
  "target": "00aeaab8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaa60`](#insn-00aeaa60)

~~~json
{
  "source": "00aeaa60",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0828",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaa88`](#insn-00aeaa88)

~~~json
{
  "source": "00aeaa88",
  "target": "00aeaaac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaab4`](#insn-00aeaab4)

~~~json
{
  "source": "00aeaab4",
  "target": "010a0830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0830",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaab8`](#insn-00aeaab8)

~~~json
{
  "source": "00aeaab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaabc`](#insn-00aeaabc)

~~~json
{
  "source": "00aeaabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
