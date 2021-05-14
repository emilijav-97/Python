
if __name__ == '__main__':
    name = 'rom_{0}x{1}.dat'

    prompt = ('--- Multiplication --- :')
    print(prompt)

    while True:
        try:
            n = int(input("Please enter the size of one operand :  "))
            print(f'Entered size is : {n}')

            file = name.format(f'{2**(2*n)}', f'{2*n}')
            fileobject = open(file, 'w')

            
            for a in range(2**n):
                for b in range(2**n):
                    p = a * b
                    
                    aa = format(a, f'0{n}b')
                    bb = format(b, f'0{n}b')
                    res = format(p, f'0{n * 2}b')

                    print(f'{res}')
                    fileobject.write(f'{res}\n')
            
            fileobject.close()
            
        except (ValueError, KeyError) as e:
            print(f'invalid value or action ({e})')

        except Exception as e:
            print(f'unknown error!{e}')

        filename = "multiplication.v"

        fileobject = open(filename,'w')
        
        fileobject.write(f"""module memory_code #(parameter N = {n})
    (input [(2*N) - 1:0] address,
    input read_en,
    input en,
    output [(2*N) - 1:0] data);
                
    reg [(2*N) - 1:0] mem [0: 2**(2*N)-1];
    assign data = (en && read_en) ? mem[address] : 0;
    
    initial begin

    $readmemb("{name}", mem);
        end
    endmodule""")

        fileobject.close()

        filename = "multiplication_tb.v"

        fileobject = open(filename,'w')
        
        fileobject.write(f"""
    `timescale 1ns / 1ps
    module mempy_TB;
    parameter N = {n};
    reg [(2*N) - 1:0] address;
    reg read_en, en;
    wire [(2*N) - 1:0] data;
 
    integer i,j;
  
memory_code dut(.address(address),
          .data(data),
          .read_en(read_en),
          .en(en));

 initial begin

   address = 0;
   read_en = 0;
   en      = 0;

   #10 $monitor ("address = %h, data = %h, read_en = %b, en = %b", address, data, read_en, en);

   for (i = 0; i < 2**(2*N); i = i + 1 )begin
     for (j = 0; j < 2**(2*N); j = j + 1)begin

     #5 address = {{i,j}};
     read_en = 1;
     en = 1;
     #5 read_en = 0;
     en = 0;
     address = 0;
    end
  end
end
endmodule""")

        fileobject.close()
        break
       
    print("---- -----")
